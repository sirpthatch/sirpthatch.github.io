---
layout: post
title: "Building Ages throughout Brooklyn"
date: 2017-03-01 20:00:00
tags: [nyc, brooklyn, pluto, construction, opendata]
---

A quick tour through different neighborhoods in Brooklyn will take you through decades of construction and building styles.  Thanks to the NYC [OpenData](https://nycopendata.socrata.com) project, and the [Pluto](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) dataset, we can put some numbers on exactly how old the builds are throughout our fair borough.  Turns out, overall, Brooklyn clocks in with the oldest original construction date amongst all the boroughs of NYC - with a median construction year of 1931 (normalized to square footage).  Manhattan is only slightly newer, at 1938.

Not surprisingly, building age is different throughout Brooklyn.  Below we plot out the median building age by census tract, normalized to square footage.

[![Brooklyn Building Ages]({{site.url}}/assets/BuildingConstruction.NormArea.CensusTract.median.2016.Brooklyn.png)]({{site.url}}/assets/BuildingConstruction.NormArea.CensusTract.median.2016.Brooklyn.png)

The oldest neighborhoods are Ocean Hill (1911) and a four way tie between North Side-South Side, Cypress Hill, Park Slope, and Styvesant Heights - all with a median building year of 1920.  The newest neighborhood is Coney Island (1969), followed by West Brighton (1962), East New York (1961), Canarsie (1960), and Williamsburg (1956).  These are using the neighborhoods defined by NYC's ["neighborhood tabulation areas"](https://data.cityofnewyork.us/City-Government/Neighborhood-Tabulation-Areas/cpf4-rkhq/data).

Of course, the median age of buildings does not tell the whole story.  When walking around a neighborhood like Park Slope you tend to notice not just that the building are old, but they are all old - there is a general consistency in the building age.  Below is a map that attempts to capture that - measuring the diversity of building ages within Brooklyn neighborhoods (high diversity is darker, more consistency in age is lighter):

[![Brooklyn Building Age Diversity]({{site.url}}/assets/BuildingConstruction.NormArea.Neighborhood.diversity.2016.Brooklyn.png)]({{site.url}}/assets/BuildingConstruction.NormArea.Neighborhood.diversity.2016.Brooklyn.png)

You can see that Park Slope is only in the middle of the pack.  Neighborhoods like Brownsville and East Flatbush have the highest degree of homogenous construction age, whereas neighborhoods like Canarsie, Williamsburg, Greenpoint, and Fort Greene have a lot of variance - some new buildings sprouting up amongst the old.

New construction will most likely change how our neighborhoods look and feel, and 10 years from now these same maps will likely be entirely different.  Brooklyn may even loose the title of the oldest borough overall.  But I would wager there will still be enclaves of untouched, original construction for years to come - you just may have to venture further out in Brooklyn to find them!

## Figure out your own home age
The statistics and figures here come from the [Pluto](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) dataset, so adventurous data enthusiasts can download the dataset themselves and search for their building.  The dataset contains a wealth of information, including building type, zoning information, square footage, etc.

For an easier option, download this file: [BK Addresses.xlsx]({{site.url}}/assets/BK Addresses.xlsx) and search for you address.  It is setup with filters at the top which should help you narrow in on your street and house number.  The file includes information on who the owner on record is, when it was built, and when it was last updated.  Happy house hunting!
