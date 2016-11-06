---
layout: post
title: "NYC General Bike Stats"
date: 2016-11-06 17:00:00
tags: [nyc, bike, safety, opendata]
---

I stumbled on a pretty awesome dump of [NYC bike stats](https://data.cityofnewyork.us/Transportation/NYCDCP-Manhattan-Bike-Counts-On-Street-Weekday/qfs9-xn8t) recently through the NYC OpenData project.  Apparently, every year on a particular day in the fall teams go out to specific locations throughout the city and collect data on a bunch of bike related measures - like how many riders, split between male and female, whether they are wearing helmets, etc.  They have been doing this consistently since 2005 in 10 locations throughout the city.  With all of those counts, make me wonder if I have ever been counted as part of this program!

### Ridership

![Ridership Over Times]({{site.url}}/assets/Ridership.png)

In general, data suggests that bike riding is on the rise in NYC.  On average, the ridership has gone up 10% year on year.  I would argue that this is conservative, and the real growth is more likely to be higher, since I am guessing that surveying was done in poor weather in some years (like 2014, where there was a 2.35% drop in ridership despite a 32% growth in 2013 and a 20.84% growth in 2015).  Ridership is growing throughout the city, but as you can see below, lower Manhattan has been pretty dominate in terms of ranking areas with the most riders.

![Ridership Rank Over Time]({{site.url}}/assets/Ridership.Rank.png)

### Gender

It is pretty clear that there are more male riders than female riders in NYC, but it is a little surprising to see just how swayed it is.  It is about 80% male versus 20% female, and while that has come down a bit from 2005 (14% female and 86% male), its not by much.

### Helmet Usage

Let me just start by saying that there is no good reason not to wear a helmet when riding a bike in NYC.  To each their own, but I question anyone's intelligence and/or sense of self worth when I see them riding around without a lid.  You can be the best cyclist in the world, but all it takes is a pedestrian staring at their iPhone stepping into the bike lane, another less coordinated cyclist clipping your wheel, or a passenger opening a door without looking to land you in the hospital.  And with a helmet, you are more likely to walk out of that hospital and ride another day.  Sermon over.

Helmet usage is pretty disappointing in NYC.  Based on the stats, it looks like only around 41% of riders wear helmets.  Women are better about it than men, with 45% of women versus 40% of men, but even 45% is pretty low as I see it.

![Helmet Utilization]({{site.url}}/assets/HelmetUsage.png)

### Bike Lane Usage

There are some good reasons not to use bike lanes sometimes (like cars parking in them), but in general I would argue that bike lane is safer than traffic.  The hierarchy might look something like: bike lane > traffic > against traffic > biking on the sidewalk.  Don't bike on the sidewalk.  Seriously.

Looks like NYC does pretty good by this measure, and is only getting better.  Most riders were counted in the bike lanes (78.15%), very few on the sidewalk (0.83%), and not many riding against traffic (3.91%).  Back in 2005, 4.09% of riders were counted on the sidewalk, so big improvement there.

![Bike Lane Utilization]({{site.url}}/assets/BikeLaneUsage.png)


A lot has been made recently about a jump in the crime rate, so I decided to take a look at the major felony rates in NYC, with the help of the [NYC OpenData project](https://data.cityofnewyork.us/).  There you can find records of all the major felonies reported, going back to 2006, with location and felony classification.  Off the bat, it is pretty easy to look at the number of crimes committed over time:

![NYC Crimes Committed]({{site.url}}/assets/CrimesOverTime.png)

As you can see, crime is down overall.  But in all honesty, I look at that graph and I see a pretty steady line, dominated by grand larceny (ie, stealing).  But, lets dive in, and look at the rates of change of individual crimes:

![NYC Crimes Rates of Change]({{site.url}}/assets/RatesOfChangeInCrimes.png)

Ok - so one conclusion to draw from this is that there is a 5.71% uptick in murders and a 5.83% uptick in rapes in 2015.  While tragic in their own right, taken in isolation I would advise that those rates are a little misleading.  If you look at the totality of the history we have, going back to 2001 at the aggregate crime level, one standard deviation for the rate of change of murders and rapes are 6.49% and 7.94%, respectively.  So that is not to say that the upticks are a good thing, because they certainly are not, but they are also not necessarily indicative of a regression in crime rates, rather they seem to be within the normal fluctuations of the system.  Contrast that with burglary rates, which dropped by over 10% in 2015 and have an annual standard deviation of 4.11%.  This is more likely a relevant drop.

### Worst Areas

![NYC Worst Areas]({{site.url}}/assets/major_crimes.2015.map.png)

The top three police precincts, ranked by total number of the 7 major felonies, are 75 (East New York, Brooklyn), 14 (Midtown South, Manhattan), and 43 (Sound View, Bronx).  If you are surprised by Midtown making the list, it is because of an extremely high count of larcenies - 16% higher than any other precinct.

### Changes in Crime Rate

![NYC Changes in Crime]({{site.url}}/assets/major_crimes.pctchange.2014.2015.map.png)

Precincts in blue have a drop in crime rate (good), whereas red has an increase in crime.  The top three police precints, ranked by the rise in total crime rates of the 7 major felonies, are 115 (Jamaica, Brooklyn), 88 (Clinton Hill, Brooklyn), and 108 (Long Island City).  

### Methodology

The map plots in this writeup are done using the [basemap package](http://matplotlib.org/basemap) from matplotlib.  NYC provides useful shapefiles for all of its census tracts, those can be found [here](https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku/data), and you can also pull down the [crime rate](https://data.cityofnewyork.us/Public-Safety/NYPD-7-Major-Felony-Incidents/hyij-8hr7) data from NYC OpenData.  I am happy to make available any raw data/code used, just ask.
