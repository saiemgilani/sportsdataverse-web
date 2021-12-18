---
title: 'cfbfastR'
date: '2021-05-10'
description: 'An R package to quickly obtain clean and tidy college football play by play data'
featured: true
topics: R,College Football,cfbfastR
recommended: sportsdataverse-node-js-module
---
# **cfbfastR** <a href='http://saiemgilani.github.io/cfbfastR'><img src='https://raw.githubusercontent.com/saiemgilani/cfbfastR/master/logo.png' align="right" height="150" /></a>

<!-- badges: start -->

[![CRAN
status](https://www.r-pkg.org/badges/version-last-release/cfbfastR?style=for-the-badge)](https://CRAN.R-project.org/package=cfbfastR)
[![CRAN
downloads](http://cranlogs.r-pkg.org/badges/grand-total/cfbfastR)](https://CRAN.R-project.org/package=cfbfastR)
[![Version-Number](https://img.shields.io/github/r-package/v/saiemgilani/cfbfastR?label=cfbfastR&logo=R&style=for-the-badge)](https://github.com/saiemgilani/cfbfastR/)
[![R-CMD-check](https://img.shields.io/github/workflow/status/saiemgilani/cfbfastR/R-CMD-check?label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/saiemgilani/cfbfastR/actions/workflows/R-CMD-check.yaml)
[![Lifecycle:maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg?style=for-the-badge&logo=github)](https://github.com/saiemgilani/cfbfastR/)
[![Contributors](https://img.shields.io/github/contributors/saiemgilani/cfbfastR?style=for-the-badge)](https://github.com/saiemgilani/cfbfastR/graphs/contributors)
[![Twitter
Follow](https://img.shields.io/twitter/follow/cfbfastR?color=blue&label=%40cfbfastR&logo=twitter&style=for-the-badge)](https://twitter.com/cfbfastR)
[![Twitter
Follow](https://img.shields.io/twitter/follow/SportsDataverse?color=blue&label=%40SportsDataverse&logo=twitter&style=for-the-badge)](https://twitter.com/SportsDataverse)
<!-- badges: end -->

The goal of [**`cfbfastR`**](https://saiemgilani.github.io/cfbfastR/) is
to provide the community with an R package for working with CFB data. It
is an R API wrapper around <https://collegefootballdata.com/>. Beyond
data aggregation and tidying ease, one of the multitude of services that
[**`cfbfastR`**](https://saiemgilani.github.io/cfbfastR/) provides is
for benchmarking open-source expected points and win probability
metrics.

## **Installation**

You can install the CRAN version of
[**`cfbfastR`**](https://cran.r-project.org/web/packages/cfbfastR/index.html)
with:

``` r
install.packages("cfbfastR")
```

You can install the released version of
[**`cfbfastR`**](https://github.com/saiemgilani/cfbfastR/) from
[GitHub](https://github.com/saiemgilani/cfbfastR) with:

``` r
# You can install using the pacman package using the following code:
if (!requireNamespace('pacman', quietly = TRUE)){
  install.packages('pacman')
}
pacman::p_load_current_gh("saiemgilani/cfbfastR", dependencies = TRUE, update = TRUE)
```

## **Breaking Changes**

[**Full News on
Releases**](https://saiemgilani.github.io/cfbfastR/news/index.html)

#### **College Football Data API Keys**

The [CollegeFootballData API](https://collegefootballdata.com/) now
requires an API key, here’s a quick run-down:

-   To get an API key, follow the directions here: [College Football
    Data Key Registration.](https://collegefootballdata.com/key)

-   Using the key: You can save the key for consistent usage by adding
    `CFBD_API_KEY=XXXX-YOUR-API-KEY-HERE-XXXXX` to your .Renviron file
    (easily accessed via
    [**`usethis::edit_r_environ()`**](https://usethis.r-lib.org/reference/edit.html)).
    Run
    [**`usethis::edit_r_environ()`**](https://usethis.r-lib.org/reference/edit.html),
    a new script will pop open named `.Renviron`, **THEN** paste the
    following in the new script that pops up (with**out** quotations)

``` r
CFBD_API_KEY = XXXX-YOUR-API-KEY-HERE-XXXXX
```

Save the script and restart your RStudio session, by clicking `Session`
(in between `Plots` and `Build`) and click `Restart R` (there also
exists the shortcut `Ctrl + Shift + F10` to restart your session). If
set correctly, from then on you should be able to use any of the `cfbd_`
functions without any other changes.

-   For less consistent usage: At the beginning of every session or
    within an R environment, save your API key as the environment
    variable `CFBD_API_KEY` (with quotations) using a command like the
    following.

``` r
Sys.setenv(CFBD_API_KEY = "XXXX-YOUR-API-KEY-HERE-XXXXX")
```

# Follow [cfbfastR](https://twitter.com/cfbfastR) and the [SportsDataverse](https://twitter.com/SportsDataverse) on Twitter and star this repo

[![Twitter
Follow](https://img.shields.io/twitter/follow/cfbfastR?color=blue&label=%40cfbfastR&logo=twitter&style=for-the-badge)](https://twitter.com/cfbfastR)
[![Twitter
Follow](https://img.shields.io/twitter/follow/SportsDataverse?color=blue&label=%40SportsDataverse&logo=twitter&style=for-the-badge)](https://twitter.com/SportsDataverse)

[![GitHub
stars](https://img.shields.io/github/stars/saiemgilani/cfbfastR.svg?color=eee&logo=github&style=for-the-badge&label=Star%20cfbfastR&maxAge=2592000)](https://github.com/saiemgilani/cfbfastR/stargazers/)

# **Our Authors**

-   [Saiem Gilani](https://twitter.com/saiemgilani)  
    <a href="https://twitter.com/saiemgilani" target="blank"><img src="https://img.shields.io/twitter/follow/saiemgilani?color=blue&label=%40saiemgilani&logo=twitter&style=for-the-badge" alt="@saiemgilani" /></a>
    <a href="https://github.com/saiemgilani" target="blank"><img src="https://img.shields.io/github/followers/saiemgilani?color=eee&logo=Github&style=for-the-badge" alt="@saiemgilani" /></a>

-   [Akshay Easwaran](https://twitter.com/akeaswaran)  
    <a href="https://twitter.com/akeaswaran" target="blank"><img src="https://img.shields.io/twitter/follow/akeaswaran?color=blue&label=%40akeaswaran&logo=twitter&style=for-the-badge" alt="@akeaswaran" /></a>
    <a href="https://github.com/akeaswaran" target="blank"><img src="https://img.shields.io/github/followers/akeaswaran?color=eee&logo=Github&style=for-the-badge" alt="@akeaswaran" /></a>

-   [Jared Lee](https://twitter.com/JaredDLee) </br>
    <a href="https://twitter.com/JaredDLee" target="blank"><img src="https://img.shields.io/twitter/follow/JaredDLee?color=blue&label=%40JaredDLee&logo=twitter&style=for-the-badge" alt="@JaredDLee" /></a>
    <a href="https://github.com/Kazink36" target="blank"><img src="https://img.shields.io/github/followers/Kazink36?color=eee&logo=Github&style=for-the-badge" alt="@Kazink36" /></a>

-   [Eric Hess](https://twitter.com/arbitanalytics) </br>
    <a href="https://twitter.com/arbitanalytics" target="blank"><img src="https://img.shields.io/twitter/follow/arbitanalytics?color=blue&label=%40arbitanalytics&logo=twitter&style=for-the-badge" alt="@arbitanalytics" /></a>
    <a href="https://github.com/ehess" target="blank"><img src="https://img.shields.io/github/followers/ehess?color=eee&logo=Github&style=for-the-badge" alt="@ehess" /></a>

# **Our Contributors (they’re awesome)**

-   [Nate Manzo](https://twitter.com/cfbnate)  
    <a href="https://twitter.com/cfbnate" target="blank"><img src="https://img.shields.io/twitter/follow/cfbnate?color=blue&label=%40cfbnate&logo=twitter&style=for-the-badge" alt="@cfbnate" /></a>
    <a href="https://github.com/natemanzo" target="blank"><img src="https://img.shields.io/github/followers/natemanzo?color=eee&logo=Github&style=for-the-badge" alt="@natemanzo" /></a>

-   [Michael Egle](https://twitter.com/deceptivespeed_)  
    <a href="https://twitter.com/deceptivespeed_" target="blank"><img src="https://img.shields.io/twitter/follow/deceptivespeed_?color=blue&label=%40deceptivespeed_&logo=twitter&style=for-the-badge" alt="@deceptivespeed_" /></a>
    <a href="https://github.com/michaelegle" target="blank"><img src="https://img.shields.io/github/followers/michaelegle?color=eee&logo=Github&style=for-the-badge" alt="@michaelegle" /></a>

-   [Jason DeLoach](https://twitter.com/CFBNumbers)  
    <a href="https://twitter.com/CFBNumbers" target="blank"><img src="https://img.shields.io/twitter/follow/CFBNumbers?color=blue&label=%40CFBNumbers&logo=twitter&style=for-the-badge" alt="@CFBNumbers" /></a>
    <a href="https://github.com/CFBNumbers" target="blank"><img src="https://img.shields.io/github/followers/CFBNumbers?color=eee&logo=Github&style=for-the-badge" alt="@CFBNumbers" /></a>

-   [Tej Seth](https://twitter.com/Tejseth41)  
    <a href="https://twitter.com/Tejseth41" target="blank"><img src="https://img.shields.io/twitter/follow/Tejseth41?color=blue&label=%40Tejseth41&logo=twitter&style=for-the-badge" alt="@Tejseth41" /></a>
    <a href="https://github.com/tejseth" target="blank"><img src="https://img.shields.io/github/followers/tejseth?color=eee&logo=Github&style=for-the-badge" alt="@tejseth" /></a>

-   [Conor McQuiston](https://twitter.com/ConorMcQ5)  
    <a href="https://twitter.com/ConorMcQ5" target="blank"><img src="https://img.shields.io/twitter/follow/ConorMcQ5?color=blue&label=%40ConorMcQ5&logo=twitter&style=for-the-badge" alt="@ConorMcQ5" /></a>
    <a href="https://github.com/mcqconor" target="blank"><img src="https://img.shields.io/github/followers/mcqconor?color=eee&logo=Github&style=for-the-badge" alt="@mcqconor" /></a>

-   [Tan Ho](https://twitter.com/_TanHo)  
    <a href="https://twitter.com/_TanHo" target="blank"><img src="https://img.shields.io/twitter/follow/_TanHo?color=blue&label=%40_TanHo&logo=twitter&style=for-the-badge" alt="@_TanHo" /></a>
    <a href="https://github.com/tanho63" target="blank"><img src="https://img.shields.io/github/followers/tanho63?color=eee&logo=Github&style=for-the-badge" alt="@tanho63" /></a>

-   [Keegan Abdoo](https://twitter.com/KeeganAbdoo)  
    <a href="https://twitter.com/KeeganAbdoo" target="blank"><img src="https://img.shields.io/twitter/follow/KeeganAbdoo?color=blue&label=%40KeeganAbdoo&logo=twitter&style=for-the-badge" alt="@KeeganAbdoo" /></a>
    <a href="https://github.com/keegan-abdoo" target="blank"><img src="https://img.shields.io/github/followers/keegan-abdoo?color=eee&logo=Github&style=for-the-badge" alt="@keegan-abdoo" /></a>

-   [Matt Spencer](https://twitter.com/Maatspencer)  
    <a href="https://twitter.com/Maatspencer" target="blank"><img src="https://img.shields.io/twitter/follow/Maatspencer?color=blue&label=%40Maatspencer&logo=twitter&style=for-the-badge" alt="@Maatspencer" /></a>
    <a href="https://github.com/Maatspencer" target="blank"><img src="https://img.shields.io/github/followers/Maatspencer?color=eee&logo=Github&style=for-the-badge" alt="@Maatspencer" /></a>

-   [Sebastian Carl](https://twitter.com/mrcaseb)  
    <a href="https://twitter.com/mrcaseb" target="blank"><img src="https://img.shields.io/twitter/follow/mrcaseb?color=blue&label=%40mrcaseb&logo=twitter&style=for-the-badge" alt="@mrcaseb" /></a>
    <a href="https://github.com/mrcaseb" target="blank"><img src="https://img.shields.io/github/followers/mrcaseb?color=eee&logo=Github&style=for-the-badge" alt="@mrcaseb" /></a>

# **Authors Emeritus - `cfbscrapR`\[archived\]**

-   [Meyappan Subbiah](https://twitter.com/msubbaiah1)  
    <a href="https://twitter.com/msubbaiah1" target="blank"><img src="https://img.shields.io/twitter/follow/msubbaiah1?color=blue&label=%40msubbaiah1&logo=twitter&style=for-the-badge" alt="@msubbaiah1" /></a>
    <a href="https://github.com/meysubb" target="blank"><img src="https://img.shields.io/github/followers/meysubb?color=eee&logo=Github&style=for-the-badge" alt="@meysubb" /></a>

-   [Parker Fleming](https://twitter.com/statsowar)  
    <a href="https://twitter.com/statsowar" target="blank"><img src="https://img.shields.io/twitter/follow/statsowar?color=blue&label=%40statsowar&logo=twitter&style=for-the-badge" alt="@statsowar" /></a>
    <a href="https://github.com/spfleming" target="blank"><img src="https://img.shields.io/github/followers/spfleming?color=eee&logo=Github&style=for-the-badge" alt="@spfleming" /></a>

# **Special Thanks**

-   [Nick Tice](https://github.com/NickTice)

## **Citations**

To cite the [**`cfbfastR`**](https://saiemgilani.github.io/cfbfastR/) R
package in publications, use:

BibTex Citation

``` bibtex
@misc{gilani_et_al_2021_cfbfastr,
  author = {Saiem Gilani and Akshay Easwaran and Jared Lee and Eric Hess},
  title = {cfbfastR: The SportsDataverse's R Package for College Football Data.},
  url = {https://saiemgilani.github.io/cfbfastR/},
  year = {2021}
}
```
