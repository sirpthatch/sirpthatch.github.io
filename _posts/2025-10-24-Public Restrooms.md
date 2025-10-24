---
layout: post
title: "1066 Public Bathrooms for 8 Million People: A dive into NYC's Restrooms"
date: 2025-10-24 08:00:00
tags: [nyc, parks, inspections, publicrestrooms]
---

Got to go?  NYC has about 1066 public restrooms that might be of use to you.  Thanks to pretty meticulous [record keeping](https://data.cityofnewyork.us/browse?Data-Collection_Data-Collection=Parks+Inspection+Program+%28PIP%29&sortBy=alpha&page=1&pageSize=20) we can get some insight into how well the restrooms service the city.  Let's dive in!

# Overall #
1066 restrooms sounds like a lot, but in fact it is pretty low for a city the size of NYC.  Looking at the 100 biggest cities in the US, NYC is ranked [93rd](https://comptroller.nyc.gov/reports/discomfort-stations-the-conditions-and-availability-of-nyc-parks-bathrooms/) in terms of restroom availability with 16 restrooms per 100,000 people (St. Paul is ranked first, with 210 restrooms per 100,000).  There are some efforts to improve this, in particular a [recent push](https://www.nytimes.com/2025/04/10/nyregion/nyc-bill-public-bathrooms.html) to nearly double the number of bathrooms by 2035, however that is going to be hampered by the high cost of building or renovating, and then maintaining, a bathroom in NYC - [some analysis](https://nycpolitics101.substack.com/p/cost-of-maintaining-public-toilets-in-nyc) puts it at $3.6M to build a restroom, and at 1000 additional restrooms needed to double, something has to change on a cost front.

Here they are scattered around the city:
![Restrooms]({{site.url}}/assets/restrooms.distribution.png)

There are some great resources for digging further on the geographic distribution of bathrooms, in particular:
  * [got2gonyc.com](https://www.got2gonyc.com/) - Theodora ("Teddy") Siegel's great map of restrooms
  * [nyrestroom.com](https://www.nyrestroom.com) - originally started in a Uber driver forum

In general, the restrooms that we have are fairly well equipped - [62%]({{site.url}}/assets/restroom.changingstations.png) of them have changing stations and 58% of them are fully accessible. 

Public restrooms are operated by several city agencies, including the transportation authority, libraries, and parks.  The parks service maintains the [majority]({{site.url}}/assets/restroom.operators.png) of them (728/1066).  In 1997 the NYC parks service started keeping records on the cleanliness of public restrooms through the [parks inspection program](https://www.nycgovparks.org/park-features/parks-inspection-program), which can give us some insight into how clean these facilities are.  Park restrooms are inspected on average [twice per year]({{site.url}}/assets/restrooms.distribution.png), and are graded for overall quality and some details like the amount of litter, graffiti, and structural issues.  Let's get into some questions you might have about NYC's potties!

# How clean are our restrooms? #
Not bad according to the data - of course, we should all manage our expectations when we walk into a public facility.  Conditions appear to have been [steadily improving]({{site.url}}/assets/restroom.inspections.quality.trend.png), with recent numbers showing that only ~15% of facilities are in unacceptable condition.  That data has a "dirty bump" in 2020, likely due to the realities of NYC during the pandemic.  The dominating features that lead to unacceptable conditions are litter and missing soap (16% of the cases each), though missing toilet paper is a common problem (7% of the cases).  

# Are men or women messier? #
An ancient question that the restroom inspection data can give us some insight into... turns out men's and women's restrooms are fairly equal in terms of conditions, with men's rooms slightly (but consistently) edging out women's rooms in terms of grime.  About 15% of men's rooms are categorized as unacceptable, versus 13.6% of women's rooms.

![Mens versus Womens]({{site.url}}/assets/restroom.inspection.men.women.spread.png)

# Does restroom cleanliness correlate with wealthy areas? #
I had a (pessimistic) hypothesis when I started this analysis that I would find a relationship between facility cleanliness and the wealth of neighborhoods.  After all, the [nicest public bathroom](https://www.nytimes.com/2017/04/05/nyregion/bryant-park-restroom-renovation.html) in NYC is located in a high end neighborhood (Bryant Park), and its renovation and its $270k/year upkeep funded by a private coalition.  That seems like an outlier though; the correlation between median income and restroom quality is directionally aligned, but weak at only 7%.  That points to a fairly equitable maintenance program.

![Correlations]({{site.url}}/assets/restrooms.correlations.png)

# Are restrooms evenly distributed in the city? #
Looks like it - controlling for population and excluding hot spots like highly visited public parks, restrooms density loosely matches population density.

![Population Density]({{site.url}}/assets/restrooms.count.per.pop.png)

# Parting Thoughts #
The public restrooms in NYC seem to be fairly distributed and managed well, but there is not enough of them, and it is not clear from the data that there is an easy answer for that.  We need to build more restrooms everywhere in the city to get us closer to top-tier cities higher in the rankings.




