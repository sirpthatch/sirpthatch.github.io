import os, sys
import pandas as pd
import csv

population_by_tract = "New_York_City_Population_By_Census_Tracts.csv"
fips_to_precinct = "precinct_blocks_key.csv"
output = "nyc.2010.population.byprecinct.csv"

print("Associating tract to precinct...")
tract_to_precinct = dict()
with open(fips_to_precinct) as handle:
  reader = csv.reader(handle)
  next(reader)
  for line in reader:
    [fips, precinct] = line
    tract = fips[5:11]
    tract_to_precinct[tract] = precinct

print("Associating precinct to population...")
precinct_to_population = dict()
with open(population_by_tract) as handle:
  reader = csv.reader(handle)
  next(reader)
  for line in reader:
    [borough, year, county, b_code, tract, population] = line
    if year == "2010":
      precinct = tract_to_precinct.get(tract,-1)
      if (precinct == -1): print("unable to match %s, %s, %s, %s"%(borough, county, b_code, tract)) 
      if (precinct not in precinct_to_population): precinct_to_population[precinct] = 0
      precinct_to_population[precinct] = precinct_to_population[precinct] + int(population)

print("Writing output...")
with open(output,"w") as w_handle:
  writer = csv.writer(w_handle)
  writer.writerow(["Precinct","Population"])
  for x in precinct_to_population.items():
    writer.writerow(x)
