---
layout: post
date: 2016-08-18
title: How to measure
tags: [quantlife, measurement]
---

The first thing to consider when planning for making data driven life insights is what data you are going to collect.  This is extremely non-trivial, and requires some careful planning and creative thought.  And I suspect everyone is going to be a little different.  But here are some thoughts that guide me.

From the outset, I recommend splitting *intrinsic* factors from *extrinsic* factors.  For a quick definition - intrinsic factors are things that cannot easily be observed externally.  Think emotions, feelings, temperment, etc.  Extrinsic factors are the opposite - mostly behaviors that can be observed/captured, often automatically.  The split is important, because down the line one avenue of investigation is to model intrinsic factors as variables that are dependent on the extrinsic factors (ie, behaviors driving feelings) and vis versa.

### Extrinsic Factors
Here are some simple things to get started with:
* __Sleep__ - Jawbone Up tracks dubiously detailed sleep records, and even if you just use the app with your phone you can track when you go to bed, when you wake up, how much sleep you get.  Those three measures are probably a sufficient start for most research, see their api [here](https://jawbone.com/up/developer).
* __Workouts__ - I am a fan of Strava for tracking my workouts, and they have a great API [here](https://strava.github.io/api/)
* __Nutrition__ - there are a lot of ways to cut this - calories, caffeine, water, alcohol, home cooked food, frequency of eating, timing of eating, etc. - and research varies.  And unless you are a fastidious food tracker, there is not a great way to capture this data unfortunately.  Most food journals have API's to pull the data down, but they all require some level of you going recording data in an app.  I have used Jawbone's [Caffeine App](https://itunes.apple.com/us/app/up-coffee/id828031130?mt=8) and their general food journal, both of which are accessible through the [api](https://jawbone.com/up/developer)
* __Weather__ - An integral environmental factor, and forecast.io has a nice [api](https://developer.forecast.io/)
* __Location__ - You are carrying a portable GPS tracker around, use it!  There is a nice opensource geofencing app called [locative](https://my.locative.io/) that may come in handy.

Also consider what derived measures you can generate from the raw data.  Given the time you go to bed and the time you wake up, you can get the total hours of sleep, for instance.  Or for more nontrivial combinations, like using location to determine if I take an afternoon walk, or by combinging the workouts with location to determine whether I take the subway to work or ride my bike.

### Intrinsic Factors
Think about the feelings or emotions that most affect you.  Things like general happiness, level of concentration, overall alertness, and motivation are some examples.  These things are necessarily things you have to capture explicitly, there is no automated measure that can read your mind.  But think about how to make it easy for yourself - it can be as simple as scoring a set of measures on a scale of 1-5 a couple of times a day and writing it down in a journal which you later upload.  For my purposes, I use the [twilio api](https://www.twilio.com/docs/) to send myself a survey a couple of times a day.

Two closing thoughts about the measurement challenge.  First, you do not have to build all of your capture avenues up front, they can evolve over time (especially the derived measures).  And second, it is way better to overcapture than undercapture, because you can always throw away useless data, whereas it can be hard/impossible to fill in lost historical data.
