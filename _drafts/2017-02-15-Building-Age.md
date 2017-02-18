---
layout: post
title: "Building Age throughout NYC"
date: 2017-02-15 20:00:00
tags: [nyc, pluto, construction, opendata]
---

Do you ever walk around NYC and wonder how old the buildings are around you?  With the help of NYC [OpenData](https://nycopendata.socrata.com) program (and the [Pluto](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) dataset in particular) we can find out!  Turns out, the median age of buildings, weighted by their square footage, is about 77 years old (the median construction year is 1940).  If we consider the last time a building was updated, this changes to 1965.  Each borough has their own age though:

![Age of Boroughs]({{site.url}}/assets/BoroughAges.png)

Brooklyn clocks in as the oldest borough, both when considering original building age (1931) and after considering updates (1941).  Manhattan is interesting, in that it is the second oldest in original construction (1938), but jumps to the most recently updated, with a median update year of 1986.  

But what about within the boroughs?  The following map plots out the median age of buildings, weighted by square footage, within each census tract in NYC where data is reported:

[![Age of Census Tracts]({{site.url}}/assets/BuildingConstruction.NormArea.CensusTract.median.2016.NYC.png)]({{site.url}}/assets/BuildingConstruction.NormArea.CensusTract.median.2016.NYC.png)

The distribution of building ages is not too surprising - within Brooklyn, you can see a concentration of newer buildings in Downtown Brooklyn, but large swaths of older construction in residential areas like Park Slope and Greenpoint.  There are some interesting trends within the map as well.  For starters, check out the upper east side versus the upper west side - looks like the east side trends 10+ years older than the west side.  Also, notice all of the new development along the waterfront in Queens, and contrast that to the waterfront in Brooklyn.  Looks like Brooklyn has some catching up to do.

Something else that stands out is that some neighborhoods are pretty consistent in building age, whereas others have blocks of new bordering blocks of old - and this is definitely observable when walking around.  If we bucket buildings into their neighborhoods and measure the distribution of ages, we can build a "vintage" map like the following, which shows neighborhoods in darker orange where there is higher diversity in building age and lighter orange where things are mostly similar in age:

[![Diversity of Neighborhoods]({{site.url}}/assets/BuildingConstruction.NormArea.Neighborhood.diversity.2016.NYC.png)]({{site.url}}/assets/BuildingConstruction.NormArea.Neighborhood.diversity.2016.NYC.png)

You can see hot spots of building age diversity, particularly in Williamsburg, Geenpoint, LIC, Astoria, Downtown Brooklyn, East New York, and Chelsea.  One likely reason for this is a lot of new developments in these areas.  Contrast that with areas further out in the boroughs, or to a lesser extent Park Slope, Midwood, and the Upper West side, where the building age is relatively homogeneous. 

New York is continually changing, so who knows what these maps will look like in 10 years.  But it is probably a pretty easy bet that the areas of newer construction will expand into their neighboring tracts, and more of Brooklyn and Queens will get a face lift.  So enjoy the old buildings while you can!


# Methodology
I used the 2016 v2 Pluto dataset for this analysis.  For most of the calculations, I chose to report things using square foot weighted medians.  Weighting by square footage gives greater weight to taller buildings, which makes sense to me as they have a commiserately bigger impact on the asestics of a neighborhood.  Median naturally filters out some of the outliers and allows us to concentrate on the meat of the distribution.  For measuring diversity, I took the standard deviation of the building ages within each neighborhood, and then normalized them between 0 and 1 using a logistic function.  
