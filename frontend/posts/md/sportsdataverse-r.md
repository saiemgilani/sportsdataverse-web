
# 

# sportsdataverse <a href='https://r.sportsdataverse.org/'><img src="https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-R/main/logo.png" align="right" width="20%" min-width="100px"/></a>

<!-- badges: start -->

[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/sportsdataverse-R?label=sportsdataverse&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/sportsdataverse-R/)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/sportsdataverse-R/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/sportsdataverse-R/actions/workflows/R-CMD-check.yaml)
[![Lifecycle:maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg?style=for-the-badge&logo=github)](https://github.com/sportsdataverse/sportsdataverse-R/)
[![Twitter
Follow](https://img.shields.io/twitter/follow/sportsdataverse?color=blue&label=%40sportsdataverse&logo=twitter&style=for-the-badge)](https://twitter.com/sportsdataverse)
[![Contributors](https://img.shields.io/github/contributors/sportsdataverse/sportsdataverse-R?style=for-the-badge)](https://github.com/sportsdataverse/sportsdataverse-R/graphs/contributors)
[![CRAN
Status](https://img.shields.io/cran/v/sportsdataverse?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=sportsdataverse)
<!-- badges: end -->

The [**`sportsdataverse`**](https://r.sportsdataverse.org) is a set of
sports data packages that work in harmony because they share common data
representations and API design. This package is designed to make it easy
to install and load multiple **`sportsdataverse`** packages in a single
step. Learn more about the **`sportsdataverse`** at
[sportsdataverse.org](https://sportsdataverse.org).

## Installation

You can install the released version of
[**`sportsdataverse`**](https://r.sportsdataverse.org) from
[GitHub](https://github.com/saiemgilani/sportsdataverse-R) with:

``` r
# You can install using the pacman package using the following code:
if (!requireNamespace('pacman', quietly = TRUE)){
  install.packages('pacman')
}
pacman::p_load_current_gh("sportsdataverse/sportsdataverse-R")
```

``` r
# Alternatively, using the devtools package:
if (!requireNamespace('devtools', quietly = TRUE)){
  install.packages('devtools')
}
devtools::install_github(repo = "sportsdataverse/sportsdataverse-R")
```

``` r
sportsdataverse::sportsdataverse_logo()
```

<center>

<img src='https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-R/main/data-raw/sportsdataverse-unicode-logo.png' align="center" width="50%" />

</center>

## Follow [**`sportsdataverse`**](https://twitter.com/sportsdataverse) on Twitter and star this repo

[![Twitter
Follow](https://img.shields.io/twitter/follow/sportsdataverse?color=blue&label=%40sportsdataverse&logo=twitter&style=for-the-badge)](https://twitter.com/sportsdataverse)

[![GitHub
stars](https://img.shields.io/github/stars/sportsdataverse/sportsdataverse-R.svg?color=eee&logo=github&style=for-the-badge&label=Star%20sportsdataverse&maxAge=2592000)](https://github.com/sportsdataverse/sportsdataverse-R/stargazers/)

## **Our Authors**

-   [Saiem Gilani](https://twitter.com/saiemgilani)  
    <a href="https://twitter.com/saiemgilani" target="blank"><img src="https://img.shields.io/twitter/follow/saiemgilani?color=blue&label=%40saiemgilani&logo=twitter&style=for-the-badge" alt="@saiemgilani" /></a>
    <a href="https://github.com/saiemgilani" target="blank"><img src="https://img.shields.io/github/followers/saiemgilani?color=eee&logo=Github&style=for-the-badge" alt="@saiemgilani" /></a>

## **Citations**

To cite the [**`sportsdataverse`**](https://r.sportsdataverse.org) R
package in publications, use:

BibTex Citation

``` bibtex
@misc{saiemgilani2021sdv,
  author = {Gilani, Saiem},
  title = {sportsdataverse: The Set of R Packages for Sports Data.},
  url = {https://r.sportsdataverse.org},
  year = {2021}
}
```

## **R Packages in the SportsDataverse**

<a href='https://R.sportsdataverse.org/'><img src='https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-R/main/man/figures/sdv-wall.png' width="90%" min-width="100px" /></a>

### [**`cfbfastR`**](https://cfbfastR.sportsdataverse.org/)

[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/cfbfastR?label=cfbfastR&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/cfbfastR)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/cfbfastR/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/cfbfastR/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/cfbfastR?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=cfbfastR)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FcfbfastR)](https://CRAN.R-project.org/package=cfbfastR)

### [**`hoopR`**](https://hoopr.sportsdataverse.org/)

[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/hoopR?label=hoopR&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/hoopR)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/hoopR/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/hoopR/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/hoopR?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=hoopR)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FhoopR)](https://CRAN.R-project.org/package=hoopR)

### [**`wehoop`**](https://wehoop.sportsdataverse.org/)

[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/wehoop?label=wehoop&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/wehoop)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/wehoop/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/wehoop/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/wehoop?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=wehoop)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2Fwehoop)](https://CRAN.R-project.org/package=wehoop)

### [**`fastRhockey`**](https://fastRhockey.sportsdataverse.org/)

[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/fastRhockey?label=fastRhockey&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/fastRhockey)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/fastRhockey/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/fastRhockey/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/fastRhockey?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=fastRhockey)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FfastRhockey)](https://CRAN.R-project.org/package=fastRhockey)

### [**`baseballr`**](https://BillPetti.github.io/baseballr/)

[![Version-Number](https://img.shields.io/github/r-package/v/BillPetti/baseballr?label=baseballr&logo=R&style=for-the-badge)](https://github.com/BillPetti/baseballr)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/BillPetti/baseballr/R-CMD-check.yaml?branch=master&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/BillPetti/baseballr/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/baseballr?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=baseballr)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2Fbaseballr)](https://CRAN.R-project.org/package=baseballr)

### [**`toRvik`**](https://andreweatherman.github.io/toRvik/)

[![Version-Number](https://img.shields.io/github/r-package/v/andreweatherman/toRvik?label=toRvik&logo=R&style=for-the-badge)](https://github.com/andreweatherman/toRvik)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/andreweatherman/toRvik/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/andreweatherman/toRvik/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/toRvik?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=toRvik)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FtoRvik)](https://CRAN.R-project.org/package=toRvik)

### [**`chessR`**](https://jaseziv.github.io/chessR/)

[![Version-Number](https://img.shields.io/github/r-package/v/jaseziv/chessR?label=chessR&logo=R&style=for-the-badge)](https://github.com/jaseziv/chessR)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/jaseziv/chessR/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/jaseziv/chessR/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/chessR?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=chessR)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FchessR)](https://CRAN.R-project.org/package=chessR)

### [**`sportyR`**](https://sportyr.sportsdataverse.org/)

[![Version-Number](https://img.shields.io/github/r-package/v/sportsdataverse/sportyR?label=sportyR&logo=R&style=for-the-badge)](https://github.com/sportsdataverse/sportyR)
[![R-CMD-check](https://img.shields.io/github/actions/workflow/status/sportsdataverse/sportyR/R-CMD-check.yaml?branch=main&label=R-CMD-Check&logo=R&logoColor=white&style=for-the-badge)](https://github.com/sportsdataverse/sportyR/actions/workflows/R-CMD-check.yaml)
[![CRAN
Status](https://img.shields.io/cran/v/sportyR?color=success&label=CRAN%20Version&logo=R&style=for-the-badge)](https://CRAN.R-project.org/package=sportyR)
[![CRAN
downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=success&label=Downloads&query=%24%5B0%5D.downloads&url=https%3A%2F%2Fcranlogs.r-pkg.org%2Fdownloads%2Ftotal%2F2021-10-26%3Alast-day%2FsportyR)](https://CRAN.R-project.org/package=sportyR)
