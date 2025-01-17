import json
import os
import re
import time
import urllib.error
from datetime import datetime
from supabase import create_client, Client

import marko
from bs4 import BeautifulSoup
import pandas as pd

import requests
import luigi
import luigi.format


BASE_DIR = "data"
supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


def download_to(url, fp):
    headers = {
        'User-Agent': 'SportsDataverse https://sportsdataverse.org / sportsdataverse@gmail.com',
    }

    if 'github.com' in url:
        headers['Authorization'] = f"token {os.environ['TOKEN']}"

    data = requests.get(url, headers=headers)
    if data.status_code == 404:
        fp.write('404')
    elif data.status_code == 200:
        fp.write(data.text)
    else:
        raise Exception(f"{data.status_code}: {data.text}")


class FetchGithubUser(luigi.Task):
    login = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/github_users/{self.login}.json")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://api.github.com/users/{self.login}",
                fp
            )


class FetchGithubPythonSetup(luigi.Task):
    run_id = luigi.Parameter()
    file = luigi.Parameter()
    repository = luigi.Parameter()
    branch = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_{self.file}")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://raw.githubusercontent.com/{self.repository}/{self.branch}/{self.file}",
                fp
            )


class FetchPyPiInfo(luigi.Task):
    run_id = luigi.Parameter()
    file = luigi.Parameter()
    repository = luigi.Parameter()
    branch = luigi.Parameter()

    def requires(self):
        return FetchGithubPythonSetup(file=self.file, repository=self.repository, branch=self.branch, run_id=self.run_id)

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/pypi.json")

    def run(self):
        with self.input().open('r') as fp:
            data = fp.read()

        with self.output().open('w') as fp:
            if data == "404":
                package_info = dict(
                    status="undefined"
                )
            else:
                regex = r'name\s*=\s*["\'](.+?)["\']'
                match = re.search(regex, data)
                if match:
                    package_name = match.group(1)
                else:
                    # TODO: fix
                    package_name = self.repository.split("/")[1]

                response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
                if response.status_code == 404:
                    package_info = dict(
                        status="not_found",
                        name=package_name
                    )
                else:
                    data = response.json()
                    package_info = dict(
                        status="found",
                        name=package_name,
                        version=data['info']['version'],
                        url=data['info']['package_url'],
                        license=data['info']['license'],
                        description=data['info']['summary']
                    )

            json.dump(package_info, fp)


class FetchGithubRDescription(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()
    branch = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_DESCRIPTION")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://raw.githubusercontent.com/{self.repository}/{self.branch}/DESCRIPTION",
                fp
            )


def parse_yaml_like(inp_data):
    key = None
    data = {}
    for line in inp_data.splitlines():
        if line.strip() == '':
            continue
        if line.lstrip() != line:
            data[key] += '\n' + line.strip()
        else:
            key, content = line.split(':', 1)
            data[key] = content.strip()
    return data


class FetchCRANInfo(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()
    branch = luigi.Parameter()

    def requires(self):
        return FetchGithubRDescription(repository=self.repository, branch=self.branch, run_id=self.run_id)

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/cran.json")

    def run(self):
        with self.input().open('r') as fp:
            data = fp.read()

        with self.output().open('w') as fp:
            if data == "404":
                package_info = dict(
                    status="undefined"
                )
            else:
                data = parse_yaml_like(data)
                name = data['Package']
                package_info = dict(
                    status='not_found',
                    name=name,
                    version=data['Version'],
                    license=data.get('License', ''),
                    description=data['Description']
                )

                CRAN_URL = "https://cran.r-project.org/package={}"
                CRAN_URL_SCRAPE = "https://mirror.lyrahosting.com/CRAN/web/packages/{}/index.html"

                url = CRAN_URL.format(name)
                try:
                    scrape_url = CRAN_URL_SCRAPE.format(name)
                    df = pd.read_html(scrape_url)
                except urllib.error.HTTPError:
                    pass
                except ValueError:
                    # https://cran.r-project.org/web/packages/mlbgameday/index.html
                    # "Package ‘mlbgameday’ was removed from the CRAN repository."
                    pass
                else:
                    data = dict(zip(df[0][0], df[0][1]))
                    package_info.update({
                        'status': 'found',
                        'url': url,
                        'version': data['Version:'],
                        'license': data['License:']
                    })

                if 'MIT' in package_info['license']:
                    package_info['license'] = 'MIT'

            if package_info['license'] == 'file LICENSE':
                del package_info['license']

            json.dump(package_info, fp)


class FetchGithubRepoInfo(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_repository.json")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://api.github.com/repos/{self.repository}",
                fp
            )


class FetchGithubRepoTree(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()
    branch = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_tree.json")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://api.github.com/repos/{self.repository}/git/trees/{self.branch}",
                fp
            )


class FetchGithubRepoContributors(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_contributors.json")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://api.github.com/repos/{self.repository}/contributors",
                fp
            )


class FetchGithubReadme(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()
    branch = luigi.Parameter()
    filename = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_{self.filename.lower()}")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://raw.githubusercontent.com/{self.repository}/{self.branch}/{self.filename}",
                fp
            )


class FetchGithubLanguage(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_languages.json")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://api.github.com/repos/{self.repository}/languages",
                fp
            )


class FetchGithubCommits(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/tmp/{self.run_id}/{self.repository.replace('/', '__')}/github_commits.json")

    def run(self):
        with self.output().open('w') as fp:
            download_to(
                f"https://api.github.com/repos/{self.repository}/commits",
                fp
            )


def determine_project_type(language, languages, package_info, files):
    if package_info['status'] == 'found':
        return language, 'package'
    elif package_info['status'] == 'not_found':
        return language, 'github_package'
    else:
        if languages.get('Jupyter Notebook', 0) > languages.get('Python', 0):
            return 'Python', 'tutorial'
        if any([file.endswith(".rmd") for file in files]):
            return 'R', 'tutorial'

        return language, 'repository'


def extract_logo_url(repository, branch, content):
    base_url = f"https://raw.githubusercontent.com/{repository}/{branch}/"
    for line in content.splitlines()[:10]:
        if '<img' in line:
            soup = BeautifulSoup(line, features="lxml")
            img = soup.find('img')
            if img:
                # if img.attrs.get('align') == "right":
                url = img.attrs.get('src')
                if url.startswith('http'):
                    return url
                else:
                    return base_url + url
    return None


def extract_images(repository, branch, content):
    images = []
    base_url = f"https://raw.githubusercontent.com/{repository}/{branch}/"

    def repl(m):
        return '[' + m.group(1).replace("\n", " ").replace("\r", " ") + ']'
    content = re.sub('\\[([^\\]]+)\\]', repl, content)

    content_html = marko.convert(content)
    for line in content_html.splitlines():
        if '<img' in line:
            soup = BeautifulSoup(line, features="lxml")
            img = soup.find('img')
            if img:
                # if img.attrs.get('align') == "right":
                url = img.attrs.get('src')
                if url.startswith('http'):
                    if url.startswith('https://github.com') or \
                            url.startswith('https://raw.githubusercontent.com') or \
                            url.startswith('https://i.imgur.com'):
                        if 'badge' in url:
                            continue

                        if 'raw' not in url:
                            url += "?raw=true"

                        images.append(url)
                else:
                    images.append(base_url + url)
    return images


def determine_sports(*inputs):
    keywords = {
        "Soccer": ["soccer", "opta", "understat", "transfermarkt", "metrica", "statsbomb", "lastrow", "wyscout", "midfielders", "kloppy"],
        "American Football": ["nfl", "football", "cfb", "big data bowl", "ptplot"],
        "Australian Football": ["afl"],
        "Ice Hockey": ["nhl", "hockey", "big data cup"],
        "Basketball": ["nba", "basketball"],
        "Baseball": ["mlb", "baseball", "retrosheet"],
        "Cricket": ["cricket"],
        "Netball": ["netball"],
        "Chess": ["chess", "lichess"],
        "Motorsport": ["f1"],
        "Cycling": ["cycling"]
    }

    sports = set()
    for input_ in inputs:
        input_ = input_.lower()
        for sport, keywords_ in keywords.items():
            for keyword in keywords_:
                if keyword in input_:
                    sports.add(sport)

    if sports == {"Soccer", "American Football"}:
        sports = {"Soccer"}
    if sports == {"American Football", "Australian Football"}:
        sports = {"Australian Football"}

    return list(sports)


class CollectProjectInfo(luigi.Task):
    run_id = luigi.Parameter()
    repository = luigi.Parameter()

    def requires(self):
        return {
            'repository': FetchGithubRepoInfo(repository=self.repository, run_id=self.run_id),
            'language': FetchGithubLanguage(repository=self.repository, run_id=self.run_id),
            'commits': FetchGithubCommits(repository=self.repository, run_id=self.run_id),
            'contributors': FetchGithubRepoContributors(repository=self.repository, run_id=self.run_id)
        }

    def output(self):
        return luigi.LocalTarget(f"{BASE_DIR}/output/{self.run_id}/{self.repository.replace('/', '__')}.json")

    def run(self):
        with self.input()['language'].open('r') as fp:
            languages = json.load(fp)

        with self.input()['commits'].open('r') as fp:
            commits = json.load(fp)

        with self.input()['contributors'].open('r') as fp:
            contributors = json.load(fp)

        with self.input()['repository'].open('r') as fp:
            repository_info = json.load(fp)
            if repository_info == 404:
                raise Exception("Repo not found")
            default_branch = repository_info['default_branch']

        tree_output = yield FetchGithubRepoTree(repository=self.repository, run_id=self.run_id, branch=default_branch)
        with tree_output.open('r') as fp:
            tree = json.load(fp)
        files = [file['path'].lower() for file in tree['tree']]

        notebook_counter = languages.get('Jupyter Notebook', 0)
        python_counter = languages.get('Python', 0) + notebook_counter
        r_counter = languages.get('R', 0)
        haskell_counter = languages.get('Haskell', 0)

        if python_counter > r_counter:
            language = "Python"
        elif r_counter > haskell_counter:
            language = "R"
        elif haskell_counter > 0:
            language = 'Haskell'
        else:
            language = 'Other'

        readme = ''
        if 'readme.md' in files:
            readme_output = yield FetchGithubReadme(
                repository=self.repository,
                run_id=self.run_id,
                branch=default_branch,
                filename='README.md' if 'readme.md' in files else 'README.rst'
            )
            with readme_output.open('r') as fp:
                readme = fp.read()

        logo_url = extract_logo_url(self.repository, default_branch, readme)
        images = [
            img for img in extract_images(self.repository, default_branch, readme)
            if img != logo_url
        ]

        package_info_output = None
        package_info = dict(
            status="undefined"
        )
        if language == "Python":
            if 'setup.py' in files:
                package_info_output = yield FetchPyPiInfo(
                    file='setup.py',
                    run_id=self.run_id,
                    repository=self.repository,
                    branch=default_branch
                )
            elif 'pyproject.toml' in files:
                package_info_output = yield FetchPyPiInfo(
                    file='pyproject.toml',
                    run_id=self.run_id,
                    repository=self.repository,
                    branch=default_branch
                )
            else:
                package_info = dict(
                    status="undefined"
                )
        elif language == 'R':
            if 'description' in files:
                package_info_output = yield FetchCRANInfo(run_id=self.run_id, repository=self.repository, branch=default_branch)
            else:
                package_info = dict(
                    status="undefined"
                )
        elif language == 'Haskell':
            package_info = dict(
                status='not_found'
            )

        if package_info_output:
            with package_info_output.open('r') as fp:
                package_info = json.load(fp)

        if package_info.get('license'):
            license_ = package_info['license']
        elif 'license' in repository_info and repository_info['license']:
            license_ = repository_info['license']['spdx_id']
            if license_ == 'NOASSERTION':
                license_ = 'Other'
        else:
            license_ = None

        language, type_ = determine_project_type(
            language,
            languages,
            package_info,
            files
        )

        urls = {
            'github': f"https://github.com/{self.repository}"
        }
        if package_info['status'] == 'found':
            if language == 'R':
                urls['cran'] = package_info['url']
            else:
                urls['pypi'] = package_info['url']
        if repository_info['homepage']:
            urls['website'] = repository_info['homepage']

        now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        package_name = package_info.get('name', os.path.basename(self.repository))
        data = {
            'name': package_name,
            'language': language,
            'license': license_,
            'latestVersion': package_info.get('version'),
            'lastCommit': {
                'sha': commits[0]['sha'],
                'date': commits[0]['commit']['committer']['date'],
                'message': commits[0]['commit']['message']
            },
            'type': type_,
            'logoUrl': logo_url,
            'description': package_info.get(
                'description',
                repository_info.get('description')
            ),
            'images': [dict(url=img) for img in images],
            'urls': urls,
            'contributors': [
                contributor['login']
                for contributor
                in contributors
            ],
            'sports': determine_sports(
                package_info.get('description', ''),
                readme,
                package_name
            ),
            'categories': [],
            'dates': {
                'created': now,
                'updated': now,
                'lastChecked': now
            }
        }

        with self.output().open('w') as fp:
            json.dump(data, fp, indent=4)


def is_project_modified(project, prev_project):
    for k, v in project.items():
        if k == 'dates':
            continue

        if k not in prev_project or prev_project[k] != v:
            return True
    return False


class CollectAll(luigi.Task):
    run_id = luigi.Parameter()
    input_file = luigi.Parameter()

    def input(self):
        return luigi.LocalTarget(self.input_file)

    def output(self):
        return {
            'projects': luigi.LocalTarget(f"../frontend/data/projects.json"),
            'users': luigi.LocalTarget(f"../frontend/data/users.json"),
        }

    def complete(self):
        # always run
        return False

    def run(self):
        projects = []
        users = {}

        categories = {
            "viz": "Visualization",
            "api": "Scraper/API",
            "scraper": "Scraper/API",
            "data": "Open-data",
            "db": "Database",
            "io": "IO (Reading/Writing)",
            "model": "Model/Calculations"
        }

        for repository in self.input().open('r'):
            print(repository)
            project_categories, repository = repository.strip().split(",")

            project_output = yield CollectProjectInfo(repository=repository, run_id=self.run_id)

            with project_output.open('r') as fp:
                project = json.load(fp)

            project['categories'] = [
                categories[cat]
                for cat in project_categories.split("|")
            ]
            projects.append(project)

            for contributor in project['contributors']:
                users[contributor] = dict(
                    login=contributor,
                    name=contributor,
                    urls={
                        'github': f"https://github.com/{contributor}"
                    }
                )

        if self.output()['projects'].exists():
            with self.output()['projects'].open('r') as fp:
                previous_data = json.load(fp)

            for project in projects:
                for prev_project in previous_data:
                    if prev_project['name'] == project['name']:
                        if not is_project_modified(prev_project, project):
                            project['dates']['updated'] = prev_project['dates']['updated']
                        project['dates']['created'] = prev_project['dates']['created']
                        break

        with self.output()['projects'].open('w') as fp:
            json.dump(projects, fp, indent=4)

        with self.output()['users'].open('w') as fp:
            json.dump(list(users.values()), fp, indent=4)


if __name__ == "__main__":
    run_id = datetime.now().date().isoformat()

    tasks = [
        CollectAll(
            input_file="data/input.txt",
            run_id=run_id
        )
    ]
    if not luigi.build(tasks, local_scheduler=True):
        print("Error: Not a local Luigi Scheduled Task")
        exit(1)
