---
layout: post
title: "NYC Population Density"
date: 2016-09-19 10:00:00
tags: [nyc, opendata]
---

Take a look a look at this map of NYC population density, based on the 2010 census:

![NYC Population Density]({{site.baseurl}}/assets/nyc.population.2010.map.png)

As you might expect?  Looking at that map forced me to invalidate some of my previously held assumptions about NYC neighborhoods.  I knew that Manhattan was likely to be the densist borough overall, however I did not realize how much more dense it is than Brooklyn!  In fact, based on this map, it appears that Brooklyn is a lot less dense than most of Queens, Staten Island, and certainly the Bronx.  That was a big surprise to me.

I was also confounded by the dense cluster in the north east corner of the Bronx.  At first I figured this was just a fluke, but I investigated separately [here](http://statisticalatlas.com/tract/New-York/Bronx-County/046201/Population) and [here](https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Census-Tracts/37cg-gxjd/data).  It appears that this census tract (tract 046201) has a very high population count, about 60% more than anything else.  I am not sure what that means, but it gives me a little pause since it is such a statistical outlier when it comes to the other tracts in NYC (much less in the rest of the country).

### Methodology

The plots in this writeup are done using the [basemap package](http://matplotlib.org/basemap) from matplotlib, and a helpful tutorial [here](http://beneathdata.com/how-to/visualizing-my-location-history/).  NYC provides useful shapefiles for all of its census tracts, those can be found [here](https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku/data), and you can also pull down the [population](https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Census-Tracts/37cg-gxjd/data) data.  In order to get reasonable midrange differentiation, I [winsorized](https://en.wikipedia.org/wiki/Winsorizing) the population density (seemed better than mapping it to a logarithmic scale, since the data is visualized with a linear color scale).  But to each his own.
