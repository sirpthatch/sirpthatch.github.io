---
layout: post
title: "Citibike Age in NYC"
date: 2016-09-08 10:00:00
tags: [cycling]
---

I regularly ride my bike to work.  I find that it is the best way to get two moderately intense workouts in a day, and besides, is significantly nicer than riding the subway (no slight on the subways, I just happen to like being outside).  I have my own bike, but since Citibike has come onto the scene here in NYC I have been seeing more and more people commuting and/or riding about the city on the blue behemoths (I prefer to call them blue whales).  I was poking around the NYC bike ridership information, and found [this amazing page](http://www.nyc.gov/html/dot/html/bicyclists/bikestats.shtml) of stats available on bikes, including a complete dump of all the citibike rides ever taken!

As a quick way to play with this data and also check out mapping libraries, I analyzed ridership age by location.  I did this using a [helpful API](https://www.fcc.gov/general/census-block-conversions-api) provided by the FCC that translates Lat/Long to FIPS coordinates (from which you can figure out census blocks and tracts), the [basemap package](http://matplotlib.org/basemap/) from matplotlib, and a helpful tutorial [here](http://beneathdata.com/how-to/visualizing-my-location-history/).

Here is my resulting map of age differences in NYC (lighter color sections correspond to younger average ridership).  The median ages range from 33 at the low end, to 44 at the high end.

[Ridership Age by Census Tract]({{site.url}}/assets/manhattan.medianage.png)

Couple of observations:
 
 * Murray Hill/East Village/Alphabet City appears to have the youngest citibike riders
 * Midtown is for old riders
 * NYC is bike, and citibike is small - it will be really interesting to see how this map evolves with the large citibike expansion that happened over the summer
 * There are some weird pockets of missing info - most likely because there are no citibikes located in those census tracts
 * General ridership is a lot older than I would expect - the median age ranges between 33 and 44.  

Small caveat - not all records have age information, so I assume you do not have to provider this data when you ssign up.  This probably introduces a bias (I can argue both ways, younger and older).  

