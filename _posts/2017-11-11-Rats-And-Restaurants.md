---
layout: post
title: "Rats and Restaurants"
date: 2017-11-11 18:00:00
tags: [nyc, rodents, resturants, 311, opendata]
---
NYC, like any city, has rats, and a lot of them - a [study](http://onlinelibrary.wiley.com/doi/10.1111/j.1740-9713.2014.00764.x/abstract) done in 2014 estimated that there are around 2 million rats who call NYC home.  Most of those rats are the exotic [Norwegian Rat](https://en.wikipedia.org/wiki/Brown_rat) (spoiler, they most likely did not actually come from Norway).  But thanks to NYC's [Open Data](https://opendata.cityofnewyork.us/) portal, we can learn a lot more about our furry little cohabitants.


We can start by filtering the [311 data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) data to see the distribution of rat sightings around the city.  In total, since 2010 there have been 78k rat sightings (and 25k mouse sightings) reported by New Yorkers.  Which borough is the most rodent infested?  That distinction goes to Brooklyn, with a combined 34k rat and mouse sightings reported.  Then comes Manhattan with 27k, the Bronx with 21k, Queens with 15k, and last is Staten Island, with only 4.5k sightings.  I guess rats don't like commuting on the Staten Island ferry.

[![Rat Sightings]({{site.url}}/assets/Rodents.RatSightings.png)]({{site.url}}/assets/Rodents.RatSightings.png) 
 

# Rats versus mice
There are more then 3x as many rat reportings as there are mice reporting in NYC.  But are they geographically distributed in the same regions?  Are there "rat territories" and "mice territories" in the city?  Turns out, yes - here is a plot of the difference in rat versus mice reporting by census tract.  Areas in red have more rats being reported, areas in blue have more mice.
[![Rat Vs Mice]({{site.url}}/assets/Rodents.RatVsMice.png)]({{site.url}}/assets/Rodents.RatVsMice.png)

Rats appear to have a firm grip on most of Manhattan and Downtown Brooklyn, but as you get further out in Brooklyn and Queens there are spots where mice run the show.

# When do rats show up?
Looks like they start scampering about around 10am, and then sightings taper off throughout the rest of the day.  Note, this is based on human reported sightings, so perhaps New Yorkers are just most startled/disgusted by them in the morning, but when the evening rolls around they are used to them.

[![Rat Time of Day]({{site.url}}/assets/Rodents.RatTimeOfDay.png)]({{site.url}}/assets/Rodents.RatTimeOfDay.png)

And rats tend to mingle when the weather is nicer outside.  Below is the chart of the number of sightings in different months of the year - rat sighting peak in July, stay steady into October, and then drop precipitously for the winter.

[![Rat Month of Year]({{site.url}}/assets/Rodents.RatMonthOfYear.png)]({{site.url}}/assets/Rodents.RatMonthOfYear.png)

# What are we doing to stop them?
Recently De Blasio kicked off a [$32 million rat reduction plan](http://www1.nyc.gov/office-of-the-mayor/news/472-17/de-blasio-administration-32-million-neighborhood-rat-reduction-plan#/0), so the rat population is definitely under attack.  NYC offers up [records](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj) of where they are doing their inspections and baitings, which allows us to isolate rat "safe zones" - areas where there are high concentrations of rat sightings, but low concentrations of inspections.  Feel free to share this with your local community rat inspector (or with your rat population, depending on whose side you are on):

[![Rat Safe Zones]({{site.url}}/assets/Rodents.RatSafeZones.png)]({{site.url}}/assets/Rodents.RatSafeZones.png)

Rats are the most aggressively hunted in Manhattan; it has the most inspections or baitings (470k).  There are spots within Brooklyn and Staten Island where there has historically been lower coverage despite high rat populations.  And overall, Brooklyn has had only the third most inspections, 225k, less than half that of Manhattan.  This runs counter to the fact that Brooklyn has 25% more rodent sightings reported than Manhattan.  Maybe an area for some of that $32 million to go?

# What cuisines do rats fancy?
Thanks to the [restaurant inspections dataset](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59/data) we can see which NYC restaurants have had a problem with rodents at some point in their operation.  Turns out, most restaurants have had an issue - 63% of all NYC restaurants have been cited at some point for either mice or rats being present in their facilities.  But which cuisines do rats prefer the most?

[![Rodent Cuisine]({{site.url}}/assets/Rodents.Cuisine.png)]({{site.url}}/assets/Rodents.Cuisine.png)

The winner is latin food, with 80% being cited for rodent problems.  Caribbean (79% cited), Delicatessen (75% cited), Indian (75% cited), and Thai (74.5% cited) round out the top five cuisine types where you are most likely to run into a rat.  Looks like rats generally stay away from juice and salad places (39% cited), as well as coffee (45% cited), and ice cream (46% cited).  

I have to admit, I was really hoping that [french food](https://en.wikipedia.org/wiki/Ratatouille_(film)) was going to be the list, but that is firmly in the middle, with 64% being cited.
 
# What are rats worst enemy?
Apparently [terriers](http://gothamist.com/2016/01/09/graphic_video_nyers_go_on_dog_hunts.php) - go figure.

