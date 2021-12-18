---
title: 'baseballr'
date: '2021-12-10'
description: 'An R package to quickly obtain clean and tidy baseball play by play data'
featured: true
topics: R,baseball,MLB,MiLB,NCAA Baseball,SportsDataverse
recommended: sportsdataverse-node-js-module
---
<!-- badges: start -->

![Lifecycle:maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg?style=for-the-badge&logo=github)
![R-CMD-check](https://img.shields.io/github/workflow/status/BillPetti/baseballr/R-CMD-check?label=R-CMD-Check&logo=R&logoColor=blue&style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/BillPetti/baseballr?style=for-the-badge)
![Version-Number](https://img.shields.io/github/r-package/v/BillPetti/baseballr?label=baseballr&logo=R&style=for-the-badge)
[![Twitter
Follow](https://img.shields.io/twitter/follow/BillPetti?color=blue&label=%40BillPetti&logo=twitter&style=for-the-badge)](https://twitter.com/BillPetti)
<!-- badges: end -->

# baseballr <a href='https://BillPetti.github.io/baseballr/'><img src='https://raw.githubusercontent.com/BillPetti/baseballr/master/man/figures/logo.png' align="right" height="139" /></a>

# `baseballr`

`baseballr` is a package written for R focused on baseball analysis. It
includes functions for scraping various data from websites, such as
FanGraphs.com, Baseball-Reference.com, and baseballsavant.com. It also
includes functions for calculating metrics, such as wOBA, FIP, and
team-level consistency over custom time frames.

You can read more about some of the functions and how to use them at its
[official site](https://billpetti.github.io/baseballr/) as well as this
[Hardball Times
article](https://www.hardballtimes.com/developing-the-baseballr-package-for-r/).

## **Installation**

You can install the released version of
[**`baseballr`**](https://github.com/BillPetti/baseballr/) from
[GitHub](https://github.com/BillPetti/baseballr) with:

``` r
# You can install using the pacman package using the following code:
if (!requireNamespace('pacman', quietly = TRUE)){
  install.packages('pacman')
}
pacman::p_load_current_gh("BillPetti/baseballr")
```

``` r
# if you would prefer devtools installation
if (!requireNamespace('devtools', quietly = TRUE)){
  install.packages('devtools')
}
# Alternatively, using the devtools package:
devtools::install_github(repo = "BillPetti/baseballr")
```

For experimental functions in development, you can install the
[development
branch](https://github.com/BillPetti/baseballr/tree/development_branch):

``` r
# install.packages("devtools")
devtools::install_github("BillPetti/baseballr", ref = "development_branch")
```

## Pull Requests

Pull request are welcome, but I cannot guarantee that they will be
accepted or accepted quickly. Please make all pull requests to the
[development
branch](https://github.com/BillPetti/baseballr/tree/development_branch)
for review.

## Functionality

The package consists of two main sets of functions: data acquisition and
metric calculation.

For example, if you want to see the standings for a specific MLB
division on a given date, you can use the `standings_on_date_bref()`
function. Just pass the year, month, day, and division you want:

``` r
library(baseballr)
standings_on_date_bref("2015-08-01", "NL East", from = FALSE)
```

    ## Data courtesy of Baseball-Reference.com. Please consider supporting Baseball-Reference by signing up for a Stathead account: https://stathead.com

    ## # A tibble: 5 x 8
    ##   Tm        W     L `W-L%` GB       RS    RA `pythW-L%`
    ##   <chr> <int> <int>  <dbl> <chr> <int> <int>      <dbl>
    ## 1 WSN      54    48  0.529 --      422   391      0.535
    ## 2 NYM      54    50  0.519 1.0     368   373      0.494
    ## 3 ATL      46    58  0.442 9.0     379   449      0.423
    ## 4 MIA      42    62  0.404 13.0    370   408      0.455
    ## 5 PHI      41    64  0.39  14.5    386   511      0.374

Right now the function works as far as back as 1994, which is when both
leagues split into three divisions.

You can also pull data for all hitters over a specific date range. Here
are the results for all hitters from August 1st through October 3rd
during the 2015 season:

``` r
data <- daily_batter_bref("2015-08-01", "2015-10-03") 
```

    ## Data courtesy of Baseball-Reference.com. Please consider supporting Baseball-Reference by signing up for a Statehead account: https://stathead.com

``` r
data %>%
  head()
```

    ##   bbref_id season             Name Age  Level          Team  G  PA  AB  R  H
    ## 1   547989   2015    Manny Machado  22 Maj-AL     Baltimore 59 266 237 36 66
    ## 2   554429   2015       Matt Duffy  24 Maj-NL San Francisco 59 264 248 33 71
    ## 3   542436   2015      Jose Altuve  25 Maj-AL       Houston 57 262 244 30 81
    ## 4   571431   2015       Adam Eaton  26 Maj-AL       Chicago 58 262 230 37 74
    ## 5   501303   2015    Shin-Soo Choo  32 Maj-AL         Texas 58 260 211 48 71
    ## 6   346793   2015 Francisco Lindor  21 Maj-AL     Cleveland 58 259 224 35 79
    ##   X1B X2B X3B HR RBI BB IBB uBB SO HBP SH SF GDP SB CS    BA   OBP   SLG   OPS
    ## 1  43  10   0 13  32 26   1  25 42   2  0  1   5  6  4 0.278 0.353 0.485 0.839
    ## 2  54  12   2  3  30 15   0  15 35   0  0  1   9  8  0 0.286 0.326 0.387 0.713
    ## 3  53  19   3  6  18 10   1   9 28   4  1  3   6 11  4 0.332 0.364 0.508 0.872
    ## 4  56  12   1  5  31 23   1  22 55   5  2  2   1  9  4 0.322 0.392 0.448 0.840
    ## 5  47  14   1  9  34 39   1  38 51   8  1  1   1  2  0 0.336 0.456 0.540 0.996
    ## 6  51  17   4  7  32 18   0  18 38   1 11  5   4 10  2 0.353 0.395 0.558 0.953

In terms of metric calculation, the package allows the user to calculate
the consistency of team scoring and run prevention for any year using
`team_consistency()`:

``` r
team_consistency(2015)
```

    ## Data courtesy of Baseball-Reference.com. Please consider supporting Baseball-Reference by signing up for a Stathead account: https://stathead.com

    ## # A tibble: 30 x 5
    ##    Team  Con_R Con_RA Con_R_Ptile Con_RA_Ptile
    ##    <chr> <dbl>  <dbl>       <dbl>        <dbl>
    ##  1 ARI    0.37   0.36          17           15
    ##  2 ATL    0.41   0.4           88           63
    ##  3 BAL    0.4    0.38          70           42
    ##  4 BOS    0.39   0.4           52           63
    ##  5 CHC    0.38   0.41          30           85
    ##  6 CHW    0.39   0.4           52           63
    ##  7 CIN    0.41   0.36          88           15
    ##  8 CLE    0.41   0.4           88           63
    ##  9 COL    0.35   0.34           7            3
    ## 10 DET    0.39   0.38          52           42
    ## # ... with 20 more rows

You can also calculate wOBA per plate appearance and wOBA on contact for
any set of data over any date range, provided you have the data
available.

Simply pass the proper data frame to `woba_plus`:

``` r
data %>%
  filter(PA > 200) %>%
  woba_plus %>%
  arrange(desc(wOBA)) %>%
  select(Name, Team, season, PA, wOBA, wOBA_CON) %>%
  head()
```

    ##                Name       Team season  PA  wOBA wOBA_CON
    ## 1 Edwin Encarnacion    Toronto   2015 216 0.490    0.555
    ## 2      Bryce Harper Washington   2015 248 0.450    0.529
    ## 3       David Ortiz     Boston   2015 213 0.449    0.541
    ## 4        Joey Votto Cincinnati   2015 251 0.445    0.543
    ## 5       Chris Davis  Baltimore   2015 253 0.434    0.617
    ## 6     Shin-Soo Choo      Texas   2015 260 0.430    0.495

You can also generate these wOBA-based stats, as well as FIP, for
pitchers using the `fip_plus()` function:

``` r
daily_pitcher_bref("2015-04-05", "2015-04-30") %>% 
  fip_plus() %>% 
  select(season, Name, IP, ERA, SO, uBB, HBP, HR, FIP, wOBA_against, wOBA_CON_against) %>%
  arrange(desc(IP)) %>% 
  head(10)
```

    ## Data courtesy of Baseball-Reference.com. Please consider supporting Baseball-Reference by signing up for a Statehead account: https://stathead.com

    ##    season            Name   IP  ERA SO uBB HBP HR  FIP wOBA_against
    ## 1    2015    Johnny Cueto 37.0 1.95 38   4   2  3 2.62        0.210
    ## 2    2015  Dallas Keuchel 37.0 0.73 22  11   0  0 2.84        0.169
    ## 3    2015      Sonny Gray 36.1 1.98 25   6   1  1 2.69        0.218
    ## 4    2015      Mike Leake 35.2 3.03 25   7   0  5 4.16        0.240
    ## 5    2015 Felix Hernandez 34.2 1.82 36   6   3  1 2.20        0.225
    ## 6    2015    Corey Kluber 34.0 4.24 36   5   2  2 2.40        0.295
    ## 7    2015   Jake Odorizzi 33.2 2.41 26   8   1  0 2.38        0.213
    ## 8    2015 Josh Collmenter 32.2 2.76 16   3   0  1 2.82        0.290
    ## 9    2015   Bartolo Colon 32.2 3.31 25   1   0  4 3.29        0.280
    ## 10   2015    Zack Greinke 32.2 1.93 27   7   1  2 3.01        0.240
    ##    wOBA_CON_against
    ## 1             0.276
    ## 2             0.151
    ## 3             0.239
    ## 4             0.281
    ## 5             0.272
    ## 6             0.391
    ## 7             0.228
    ## 8             0.330
    ## 9             0.357
    ## 10            0.274

The `edge_scrape()` function allows the user to scrape PITCHf/x data
from the GameDay application using Carson Sievert’s
[pitchRx](https://github.com/cpsievert/pitchRx) package and to calculate
metrics associated with
[Edge%](https://billpetti.shinyapps.io/edge_shiny/). The function
returns a dataframe grouped by either pitchers or batters and the
percentge of pitches in each of the various Edge zones.

Example (pitchers):

``` r
library(dplyr)
edge_scrape("2015-04-06", "2015-04-07", "pitcher") %>% 
  select(-6:-4, -13) %>% 
  head(10)
```

Example (batters):

``` r
edge_scrape("2015-04-06", "2015-04-07", "batter") %>% 
  select(-6:-4, -13) %>% 
  head(10)
```

More functionality will be added soon. Please leave any suggestions or
bugs in the [Issues
section](https://github.com/BillPetti/baseballr/issues).

## Follow the [SportsDataverse](https://twitter.com/SportsDataverse) on Twitter and star this repo

[![Twitter
Follow](https://img.shields.io/twitter/follow/SportsDataverse?color=blue&label=%40SportsDataverse&logo=twitter&style=for-the-badge)](https://twitter.com/SportsDataverse)

[![GitHub
stars](https://img.shields.io/github/stars/billpetti/baseballr.svg?color=eee&logo=github&style=for-the-badge&label=Star%20baseballr&maxAge=2592000)](https://github.com/billpetti/baseballr/stargazers/)

## **Our Authors**

-   [Bill Petti](https://twitter.com/BillPetti)  
    <a href="https://twitter.com/BillPetti" target="blank"><img src="https://img.shields.io/twitter/follow/BillPetti?color=blue&label=%40BillPetti&logo=twitter&style=for-the-badge" alt="@BillPetti" /></a>
    <a href="https://github.com/BillPetti" target="blank"><img src="https://img.shields.io/github/followers/BillPetti?color=eee&logo=Github&style=for-the-badge" alt="@BillPetti" /></a>

## **Our Contributors (they’re awesome)**

-   [Ben Baumer](https://twitter.com/BaumerBen)  
    <a href="https://twitter.com/BaumerBen" target="blank"><img src="https://img.shields.io/twitter/follow/BaumerBen?color=blue&label=%40BaumerBen&logo=twitter&style=for-the-badge" alt="@BaumerBen" /></a>
    <a href="https://github.com/beanumber" target="blank"><img src="https://img.shields.io/github/followers/beanumber?color=eee&logo=Github&style=for-the-badge" alt="@beanumber" /></a>

-   [Ben Dilday](https://twitter.com/BenDilday)  
    <a href="https://twitter.com/BenDilday" target="blank"><img src="https://img.shields.io/twitter/follow/BenDilday?color=blue&label=%40BenDilday&logo=twitter&style=for-the-badge" alt="@BenDilday" /></a>
    <a href="https://github.com/bdilday" target="blank"><img src="https://img.shields.io/github/followers/bdilday?color=eee&logo=Github&style=for-the-badge" alt="@bdilday" /></a>

-   [Robert Frey](https://twitter.com/RobertFrey40)  
    <a href="https://twitter.com/RobertFrey40" target="blank"><img src="https://img.shields.io/twitter/follow/RobertFrey40?color=blue&label=%40RobertFrey40&logo=twitter&style=for-the-badge" alt="@RobertFrey40" /></a>
    <a href="https://github.com/robert-frey" target="blank"><img src="https://img.shields.io/github/followers/robert-frey?color=eee&logo=Github&style=for-the-badge" alt="@robert-frey" /></a>

-   [Saiem Gilani](https://twitter.com/saiemgilani)  
    <a href="https://twitter.com/saiemgilani" target="blank"><img src="https://img.shields.io/twitter/follow/saiemgilani?color=blue&label=%40saiemgilani&logo=twitter&style=for-the-badge" alt="@saiemgilani" /></a>
    <a href="https://github.com/saiemgilani" target="blank"><img src="https://img.shields.io/github/followers/saiemgilani?color=eee&logo=Github&style=for-the-badge" alt="@saiemgilani" /></a>