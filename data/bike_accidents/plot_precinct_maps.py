import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon
from shapely.prepared import prep
import fiona
from matplotlib.collections import PatchCollection
from descartes import PolygonPatch
import json
import datetime
import csv, os

population = pd.read_csv("nyc.2010.population.byprecinct.csv")
bike_accidents = pd.read_csv("bike.car.2015.csv")
bike_accidents.columns = [x.strip() for x in bike_accidents.columns]
output_name = "bike.car.2015.map.png"
title = "Accident Rates btw Bike and Car in 2015"

shapefilename = "geo_export_60e803f0-6968-4766-9119-0cb262730d9f"
print("Reading block -> median age file...")
tract_to_median = dict()

print("Loading basemap...")
with fiona.open(shapefilename+'.shp') as shp:
  coords = shp.bounds

#full_map = [-74.2555913638106, 40.49611539521161, -73.7000090638712, 40.91553277600008]
#manhattan_map = [-74.0555913638106, 40.69582408560584, -73.9000090638712, 40.88553277600008]
#coords = manhattan_map

w, h = coords[2] - coords[0], coords[3] - coords[1]
extra = 0.01

lon_0=np.mean([coords[0], coords[2]])
lat_0=np.mean([coords[1], coords[3]])
llcrnrlon=coords[0] - extra * w
llcrnrlat=coords[1] - (extra * h)
urcrnrlon=coords[2] + extra * w
urcrnrlat=coords[3] + (extra * h)

m = Basemap(
      projection='tmerc', ellps='WGS84',
      lon_0=lon_0,
      lat_0=lat_0,
      llcrnrlon=llcrnrlon,
      llcrnrlat=llcrnrlat,
      urcrnrlon=urcrnrlon,
      urcrnrlat=urcrnrlat,
      resolution='i',
      suppress_ticks=True)

_out = m.readshapefile(shapefilename, name='nyc', drawbounds=False, color='none', zorder=2)
print(m.nyc_info[0])

print("Pivoting crash data")
j_pop_crash = bike_accidents.set_index("Precinct").join(population.set_index("Precinct"))
j_pop_crash["crashes_per_thousand"] = j_pop_crash["Crashes"] / (j_pop_crash["Population"]/1000.0)
cap = j_pop_crash.crashes_per_thousand.quantile(.9)
j_pop_crash["capped_crashes_per_thousand"] = j_pop_crash.crashes_per_thousand.apply(lambda x: min(cap, x))
print(j_pop_crash.head())

def get_crash_rate(precinct):
  precinct = int(precinct)
  if precinct in j_pop_crash.index:
    return j_pop_crash.loc[precinct]["capped_crashes_per_thousand"]
  else: return 0

print("Building dataframe from map")
df_map = pd.DataFrame({
      'poly': [Polygon(blocks) for blocks in m.nyc],
      'crash_rate': [get_crash_rate(x["precinct"]) for x in m.nyc_info]})
df_map = df_map.fillna(0)
print(df_map.head())

print("Building image")
figwidth = 14
fig = plt.figure(figsize=(figwidth, figwidth*h/w))
ax = fig.add_subplot(111, axisbg='w', frame_on=False)
cmap = plt.get_cmap('Reds')
#cmap = plt.get_cmap('hsv')
#cmap = plt.get_cmap('gist_rainbow')

# draw neighborhoods with grey outlines
df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(x, ec='#111111', lw=.8, alpha=.6, zorder=4))
pc = PatchCollection(df_map['patches'], match_original=True)

min_level = 0 
max_level = df_map["crash_rate"].max()


print("Min and Max Rate: [%s,%s]"%(min_level, max_level))
cmap_list = [x for x in df_map.crash_rate.apply(lambda x: (0,0,0,0) if x == 0 else cmap((x * 1.0 - min_level)/(max_level - min_level)))] 
#cmap_list = [cmap(max(0, min(1,val))) for val in (df_map.median_age.values - 0)/65]
#cmap_list = [cmap(x*1.0/len(all_tracts)) for x in df_map.tract.apply(lambda y:all_tracts.index(y))]
pc.set_facecolor(cmap_list)
ax.add_collection(pc)
m.drawmapboundary(ax=ax, zorder=5)

fig.suptitle(title, fontdict={'size':24, 'fontweight':'bold'}, y=0.92)
#plt.show()
plt.savefig(output_name, dpi=100, frameon=False, bbox_inches='tight', pad_inches=0.5, facecolor='#F2F2F2')


