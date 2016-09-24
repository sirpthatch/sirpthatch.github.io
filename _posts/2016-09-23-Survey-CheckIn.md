---
layout: post
title: "Survey Checkin"
date: 2016-09-23 22:00:41
tags: [quantlife, survey]
---

Of all the services that I have running to pull down data on my life, the survey system is arguably the most important.  Ultimately, a major goal is to eventually be able to predict things like my happiness and concentration, and perhaps even help guide them.  As such, finding a high quality way to pull down data on my mental state is important.

To achieve this, I have a very simple service that periodically sends me a predefined survey in a text message, to which I respond with measures for how happy, alert, and concetrated I am at that particular moment.  The survey times are somewhat random, but garaunteed to be delivered throughout the day.

My analysis is only going to be effective if I get sufficient data, though I need to be realistic in that I cannot expect to answer my survey every 10 minutes.   Or even every couple of hours.  Realistically, sometimes I just do not want to respond.  The survey system understands this, and through a response feedback loop will decrease or increase its question frequency based on my engagement level.

So, that said, what does it look like so far?  I have some interesting results, nothing ground breaking so far.  First, when it comes to responding, I am most likely to respond to my surveys in the afternoon - 33% of my responses came between 1 and 5, compared to only 20% coming in the morning.  When it comes to my survey itself, ideally I wanted to pick indepent attributes, with low correlations.  It looks like I mostly achieved this - the correlation between most pairs is around 35%, however the correlation between concentration and happiness is around 50%.  That is in someway an interesting result in of itself, however it probably means I need to redesign the survey to have more independence in the measures.

There are two early questions that I wanted to answer:

1. Am I a morning person?
2. Does biking to work make my day better?

### Am I morning person?
So far it is a little hard to tell, but early indications suggest that I have a minor (1%) lift in concentration in the morning, despite having a negative 3% draw on alertness.  I can qualitatively corroborate this, however I will be interested to see how this evolves as more data comes in.  Also worth noting - while the data suggest I concentrate the most in the morning, it is clear that I am happiest in the evening, with an 11% lift in happiness coming after 6pm (morning is ok, and then there is a big dip midday).

### Does biking to work make my day better?
It looks like there is some immediate impact, but it wears off pretty quickly.  On days that I bike to work, I experience about a 3% bump in happiness, and a 6% bump in concentration.  That said, over the course of the whole day it averages out, and the only affect at the day level might be a slight uptick in volatility in all the measures.  But it appears to be minor and may just be noise at the moment.

So where to go from here?  I may need to tweak my survey to measure a more differentiated set of attributes, and I need to find a way to bump up my midday happiness (I am starting a new job soon, will be interesting to see what impact that has on this midday lull).
