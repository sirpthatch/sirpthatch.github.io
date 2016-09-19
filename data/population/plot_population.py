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

population = pd.read_csv("New_York_City_Population_By_Census_Tracts.csv", dtype=str)
output_name = "nyc.raw.population.2010.map.png"
title = "NYC Population"

shapefilename = "geo_export_c19fb10e-b5b8-4445-9878-3350388b25bc"

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

population = population[population.Year == "2010"]
population["btract"] = population["DCP Borough Code"]+population["Census Tract"]

btract_to_population = population.set_index("btract")["Population"]

print("Building dataframe from map")
df_map = pd.DataFrame({
      'poly': [Polygon(blocks) for blocks in m.nyc],
      'btract':[x["boro_code"] + x["ct2010"] for x in m.nyc_info],
      'area':[x["shape_area"] for x in m.nyc_info]
      })
df_map["population"] = df_map["btract"].apply(lambda x:int(btract_to_population.loc[x]))
df_map["pop_density"] = df_map["population"]/df_map["area"]
df_map = df_map.fillna(0)
print(df_map.head())

print("Building image")
figwidth = 14
fig = plt.figure(figsize=(figwidth, figwidth*h/w))
ax = fig.add_subplot(111, axisbg='w', frame_on=False)
cmap = plt.get_cmap('Blues')
#cmap = plt.get_cmap('hsv')
#cmap = plt.get_cmap('gist_rainbow')

# draw neighborhoods with grey outlines
df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(x, ec='#111111', lw=.4, alpha=.1, zorder=4))
pc = PatchCollection(df_map['patches'], match_original=True)

lower_quantile = df_map["pop_density"].quantile(0.025)
upper_quantile = df_map["pop_density"].quantile(0.975)

df_map["norm_pop_density"] = df_map["pop_density"].apply(lambda x:min(upper_quantile, max(x, lower_quantile)))

min_level = df_map["norm_pop_density"].min()
max_level = df_map["norm_pop_density"].max()


print("Min and Max Rate: [%s,%s]"%(min_level, max_level))
cmap_list = [x for x in df_map.norm_pop_density.apply(lambda x: (0,0,0,0) if x == 0 else cmap((x * 1.0 - min_level)/(max_level - min_level)))] 
#cmap_list = [cmap(max(0, min(1,val))) for val in (df_map.median_age.values - 0)/65]
#cmap_list = [cmap(x*1.0/len(all_tracts)) for x in df_map.tract.apply(lambda y:all_tracts.index(y))]
pc.set_facecolor(cmap_list)
ax.add_collection(pc)
m.drawmapboundary(ax=ax, zorder=5)

fig.suptitle(title, fontdict={'size':24, 'fontweight':'bold'}, y=0.92)
#plt.show()
plt.savefig(output_name, dpi=200, frameon=False, bbox_inches='tight', pad_inches=0.5, facecolor='#F2F2F2')


