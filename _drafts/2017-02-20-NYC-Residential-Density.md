---
layout: post
title: "Residential Density in NYC"
date: 2017-02-20 20:00:00
tags: [nyc, pluto, construction, opendata]
---

New York City has about 8.4 million people living within the 5 boroughs, and about 5,4 billion square feet of total building space.  Sounds like a lot, but when you break this down to areas zoned for residential living, it averages out to about 531 square feet per person in the city as a whole.  This is not country living, but still, on a whole, not bad.  That said, with a place like NYC, averages often tell a misleading story, and this is certainly true when looking at how much living space people have throughout the city.

{:.noresize}
[![Top and Bottom Housing]({{site.url}}/assets/TopAndBottomHousingSizes.png)]({{site.url}}/assets/TopAndBottomHousingSizes.png)

Manhattan tops the charts, with 4 of the 5 neighborhoods with the highest space per person.  At the highest overall is the Upper East Side/Carnegie Hill area, with more than 1,200 square feet per person.  This is followed by Midtown (920 sq ft/person), Battery Park City (838 sq ft/person), SoHo/Tribeca (774 sq ft/person), and finally Tody Hill, Staten Island (756 sq ft/person).  Brooklyn and Queens have the most compact living spaces, with North Corona bottoming the list at 207 sq ft per person.  The other compressed spaces are Sunset Park East (246 sq ft/person), Cypress Hill (252 sq ft/person), Sunset Park West (262 sq ft/person), and Corona (266 sq ft/person).

Take a look at the city at large though:

[![Living Space in NYC]({{site.url}}/assets/ResidentialSpacePerPerson.2016.NYC.png)]({{site.url}}/assets/ResidentialSpacePerPerson.2016.NYC.png)

It does not take much to notice that lower Manhattan dominates in terms of living space.  This is counter intuitive at first - it certainly runs counter to the [population density]({{site.url}}/post/Population-Density-NYC/) map of NYC, where lower Manhattan ranks with some of the higest density in all of NYC.  Take a look at the following map though, which shows the average number of people per household throughout the city:

[![Household Size in NYC]({{site.url}}/assets/HousholdSize.2016.NYC.png)]({{site.url}}/assets/HousholdSize.2016.NYC.png)

Side by side, the map of residential space and household size almost look like inverse images.  It looks like this accounts for most of the differences across the city - apartment sizes stay pretty constant, but the number of people in the apartment varies.  In areas with a lot of children, or where parents live with their grown children, the square footage per person drops percipitously.  Throughout Manhattan this is surprisingly low (just over 1 person per household), whereas it grows to 3-4 people per household further out in the boroughs.  Note, these numbers are according to the Census ACS survey, and I am guessing do not account for roommates.  I do not buy that Manhattan averages such a low household size.  But even still, it is representative of a larger trend, of increasing household size the further out in the city you go.

As a final note, I will point out that if you consider just the land mass of the United States as a whole, there is roughly 332 thousand square feet per person currently.  Makes that NYC 531 square feet average seem like small potatoes.  But where else can you find bodegas open at 2am?

# Methodology
I used the 2016 v2 [Pluto](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) and the Census [ACS](https://www.census.gov/programs-surveys/acs/) datasets for this analysis.  I generally cleaned the data prior to aggregation by filtering out obvious outliers.  Interestingly, this included several cemetaries throughout the city, which creepily enough ended up with around 8 sq ft per person after running the numbers.  I could dig into that anomaly more, but to be honest, I am going to leave at that.
