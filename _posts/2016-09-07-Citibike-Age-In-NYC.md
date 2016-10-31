---
layout: post
title: "Citibike Age in NYC"
date: 2016-09-07 10:00:00
tags: [cycling]
---

I regularly ride my bike to work.  I find that it is the best way to get two moderately intense workouts in a day, and besides, is significantly nicer than riding the subway (no slight on the subways, I just happen to like being outside).  I have my own bike, but since Citibike has come onto the scene here in NYC I have been seeing more and more people commuting and/or riding about the city on the blue behemoths (I prefer to call them blue whales).  I was poking around the NYC bike ridership information, and found [this amazing page](http://www.nyc.gov/html/dot/html/bicyclists/bikestats.shtml) of stats available on bikes, including a complete dump of all the citibike rides ever taken!  That is close to 30 million rides so far, thanks Citibike!

The data can be split in a lot of different ways, however I focused in on rider age and its relation to geography and time.  Some surprising patterns emerged.  Most notably, Citibike riders are a lot older than I expected!  The weekday median age is 38, while the weekend median age is 35 (the overall median age in NYC is 36).  I find it a little surprising that weekend ridership is significantly lower than weekday ridership - my hypothesis is that commuters are in general older than joy riders, which is responsible for tipping the scales here.

Another interesting look at the age of citibike riders is by geography.  Below is a choloropeth of the overall median age of riders around the city (by where they start their rides, darker is older, range is between 44 years old in the darkest to 33 in the lightest):

![Ridership Age by Census Tract]({{site.baseurl}}/assets/nyc.age.png){:class="img-responsive"}

As expected, it is far from an even distribution.  Midtown and the Upper West Side have the oldest riders (median age is 44), whereas Murray Hill, East Village, and Alphabet city tend towards younger riders (median age is 33).

Certain areas (like around midtown or the financial district) are naturally going to have a higher concentation of commute related rides.  By plotting the age of weekday riders versus weekend riders, it is pretty clear that the age distribution in those neighborhoods change the most, supporting the idea that commuters trend older than the average rider:

![Weekday Ridership Age by Census Tract]({{site.baseurl}}/assets/nyc.age.weekday.png)
![Weekend Ridership Age by Census Tract]({{site.baseurl}}/assets/nyc.age.weekend.png)

And to further drive the point home, if you take into account time of day, you can see that morning riders (during commute hours) trend much older than night time riders (after 8pm).  In fact, night time riders look a lot like the weekend riders (at least age wise).

![Weekday Morning Ridership Age by Census Tract]({{site.baseurl}}/assets/nyc.age.weekday.earlymorning.png)
![Weekday Evening Ridership Age by Census Tract]({{site.baseurl}}/assets/nyc.age.weekday.night.png)

NYC is an interesting place partly because it is non-homogenous, and you can definitely see that with respect to the age of citibike riders around the city.  With the expansion of the citibike program this summer, particularly into more residential neighborhoods, I am excited to see how it evolves!

### Methodology

The plots in this writeup are done using the [basemap package](http://matplotlib.org/basemap) from matplotlib, and a helpful tutorial [here](http://beneathdata.com/how-to/visualizing-my-location-history/).  The citibike data providers lat/long coordinates of starting and ending stations, which can in turn be translated into FIPS coordinates (ie, census tracts/blocks) using this FCC provided [API](https://www.fcc.gov/general/census-block-conversions-api).  NYC provides useful shapefiles for all of its census tracts, those can be found [here](https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku/data).  

Not all records have age information, so I assume you do not have to provider this data when you sign up.  This might introduce a bias in the data (I can argue both ways, younger and older).  For this analysis, those records are just filtered out.

