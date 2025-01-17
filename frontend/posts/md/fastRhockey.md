
# 

# fastRhockey <a href='http://fastrhockey.sportsdataverse.org/'><img src='https://raw.githubusercontent.com/sportsdataverse/fastRhockey/main/logo.png' align="right" width="20%" min-width="100" /></a>

<!-- badges: start -->

[![CRAN
version](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=CRAN%20version&prefix=v&query=%24.Version&url=https%3A%2F%2Fcrandb.r-pkg.org%2FfastRhockey)](https://CRAN.R-project.org/package=fastRhockey)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FfastRhockey)](https://CRAN.R-project.org/package=fastRhockey)
[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/fastRhockey?label=fastRhockey&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/fastRhockey/)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/fastRhockey/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/fastRhockey/actions/workflows/R-CMD-check.yaml)
[![Lifecycle:maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg?style=for-the-badge&logo=github)](https://github.com/sportsdataverse/fastRhockey/)
[![Contributors](https://img.shields.io/github/contributors/sportsdataverse/fastRhockey?style=for-the-badge)](https://github.com/sportsdataverse/fastRhockey/graphs/contributors)
<!-- badges: end -->

[`fastRhockey`](https://github.com/sportsdataverse/fastRhockey) is an R
Package that is designed to pull play-by-play (and boxscore) data from
the newest version of the [Premier Hockey Federation (PHF)
website](https://www.premierhockeyfederation.com/). In the past, there
have been a few scrapers for the PHF (formerly the NWHL), but they have
all been deprecated since the league changed website formats.

With the seventh season of the league kicking off on November 6th, and
games being broadcast on ESPN+, this package was created to allow access
to play-by-play data to continue pushing women’s hockey analytics
forward.

In Spring of 2021, the [Big Data
Cup](https://www.theicegarden.com/2021/4/15/22374981/a-directory-of-womens-hockey-projects-from-big-data-cup-2021-analytics-otthac-stathletes)
and the [data they made
available](https://github.com/bigdatacup/Big-Data-Cup-2021)
revolutionized what we were able to thanks to the detailed play-by-play
data for the season and the x/y location data. That wave continued with
the inaugural [WHKYHAC conference](https://www.whkyhac.com/) in July
that produced some amazing conversations and projects in the women’s
hockey space.

In the past, the lack of data and poor access to data have been the
biggest barrier to entry in women’s hockey analytics, a barrier that
this package intends to alleviate.

<center>

<img src='https://raw.githubusercontent.com/sportsdataverse/fastRhockey/main/man/figures/fastRhockey_full_holographic_graphic.png' width="70%" />

</center>

------------------------------------------------------------------------

## Installation

You can install the CRAN version of
[**`fastRhockey`**](https://CRAN.R-project.org/package=fastRhockey)
with:

``` r
install.packages("fastRhockey")
```

You can install the released version of
[**`fastRhockey`**](https://github.com/sportsdataverse/fastRhockey/)
from [GitHub](https://github.com/sportsdataverse/fastRhockey) with:

``` r
# You can install using the pacman package using the following code:
if (!requireNamespace('pacman', quietly = TRUE)){
  install.packages('pacman')
}
pacman::p_load_current_gh("sportsdataverse/fastRhockey", dependencies = TRUE, update = TRUE)
```

If you would prefer the `devtools` installation:

``` r
if (!requireNamespace('devtools', quietly = TRUE)){
  install.packages('devtools')
}
devtools::install_github(repo = "sportsdataverse/fastRhockey")
```

------------------------------------------------------------------------

## Documentation

You can find the
[documentation](https://fastRhockey.sportsdataverse.org/) for
[**`fastRhockey`**](https://github.com/sportsdataverse/fastRhockey) on
[GitHub pages](https://fastRhockey.sportsdataverse.org/).

You can view CSVs of historical boxscore and play-by-play on the
[**`fastRhockey`**](https://github.com/sportsdataverse/fastRhockey/)
[data repo](https://github.com/sportsdataverse/fastRhockey-data), as
well as the process for scraping that historical data.

------------------------------------------------------------------------

## Breaking Changes

[**Full News on
Releases**](http://fastrhockey.sportsdataverse.org/news/index.html)

------------------------------------------------------------------------

## Follow the [SportsDataverse](https://twitter.com/sportsdataverse) on Twitter and star this repo

[![Twitter
Follow](https://img.shields.io/twitter/follow/sportsdataverse?color=blue&label=%40sportsdataverse&logo=twitter&style=for-the-badge)](https://twitter.com/sportsdataverse)

[![GitHub
stars](https://img.shields.io/github/stars/sportsdataverse/fastRhockey.svg?color=eee&logo=github&style=for-the-badge&label=Star%20fastRhockey&maxAge=2592000)](https://github.com/sportsdataverse/fastRhockey/stargazers/)

## **Our Authors**

-   [Ben Howell](https://twitter.com/BenHowell71)  
    <a href="https://twitter.com/BenHowell71" target="blank"><img src="https://img.shields.io/twitter/follow/BenHowell71?color=blue&label=%40BenHowell71&logo=twitter&style=for-the-badge" alt="@BenHowell71" /></a>
    <a href="https://github.com/BenHowell71" target="blank"><img src="https://img.shields.io/github/followers/BenHowell71?color=eee&logo=Github&style=for-the-badge" alt="@BenHowell71" /></a>

-   [Saiem Gilani](https://twitter.com/saiemgilani)  
    <a href="https://twitter.com/saiemgilani" target="blank"><img src="https://img.shields.io/twitter/follow/saiemgilani?color=blue&label=%40saiemgilani&logo=twitter&style=for-the-badge" alt="@saiemgilani" /></a>
    <a href="https://github.com/saiemgilani" target="blank"><img src="https://img.shields.io/github/followers/saiemgilani?color=eee&logo=Github&style=for-the-badge" alt="@saiemgilani" /></a>

## **Our Contributors (they’re awesome)**

-   [Alyssa Longmuir](https://twitter.com/alyssastweeting)  
    <a href="https://twitter.com/alyssastweeting" target="blank"><img src="https://img.shields.io/twitter/follow/alyssastweeting?color=blue&label=%40alyssastweeting&logo=twitter&style=for-the-badge" alt="@alyssastweeting" /></a>
    <a href="https://github.com/Aklongmuir" target="blank"><img src="https://img.shields.io/github/followers/Aklongmuir?color=eee&logo=Github&style=for-the-badge" alt="@Aklongmuir" /></a>
-   [Tan Ho](https://twitter.com/_TanHo)  
    <a href="https://twitter.com/_TanHo" target="blank"></a>
    <a href="https://github.com/tanho63" target="blank"><img src="https://img.shields.io/github/followers/tanho63?color=eee&logo=Github&style=for-the-badge" alt="@tanho63" /></a>

## **Citations**

To cite the
[**`fastRhockey`**](https://fastRhockey.sportsdataverse.org/) R package
in publications, use:

BibTex Citation

``` bibtex
@misc{howell_gilani_fastRhockey_2021,
  author = {Ben Howell and Saiem Gilani},
  title = {fastRhockey: The SportsDataverse's R Package for Hockey Data.},
  url = {https://fastRhockey.sportsdataverse.org/},
  year = {2021}
}
```
