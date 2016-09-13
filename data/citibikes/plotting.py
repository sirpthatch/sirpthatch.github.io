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


input_data = [
  ["medianage.tract.csv", "nyc.age.png", "Median Age"],
  ["medianage.weekday.tract.csv", "nyc.age.weekday.png", "Weekday Median Age"],
  ["medianage.weekeday.afternoon.tract.csv", "nyc.age.weekday.afternoon.png", "Weekday Afternoon Median Age"],
  ["medianage.weekeday.earlymorning.tract.csv", "nyc.age.weekday.earlymorning.png", "Weekday Early Morning Median Age"],
  ["medianage.weekeday.evening.tract.csv", "nyc.age.weekday.evening.png", "Weekday Evening Median Age"],
  ["medianage.weekeday.morning.tract.csv", "nyc.age.weekday.morning.png", "Weekday Morning Median Age"],
  ["medianage.weekeday.night.tract.csv", "nyc.age.weekday.night.png", "Weekday Night Median Age"],
  ["medianage.weekend.tract.csv", "nyc.age.weekend.png", "Weekend Median Age"],
  ["medianage.weekeend.afternoon.tract.csv", "nyc.age.weekend.afternoon.png", "Weekend Afternoon Median Age"],
  ["medianage.weekeend.earlymorning.tract.csv", "nyc.age.weekend.earlymorning.png", "Weekend Early Morning Median Age"],
  ["medianage.weekeend.evening.tract.csv", "nyc.age.weekend.evening.png", "Weekend Evening Median Age"],
  ["medianage.weekeend.morning.tract.csv", "nyc.age.weekend.morning.png", "Weekend Morning Median Age"],
  ["medianage.weekeend.night.tract.csv", "nyc.age.weekend.night.png", "Weekend Night Median Age"]
]

def build_choloropath(basename, output_name, title):
  input_tract_file = os.path.join("daypart_analysis", basename)
  shapefilename = "geo_export_c19fb10e-b5b8-4445-9878-3350388b25bc"
  print("Reading block -> median age file...")
  tract_to_median = dict()

  with open(input_tract_file) as handle:
    reader = csv.reader(handle)
    for line in reader:
      block = line[0]
      if line[1]:
        tract_to_median[block] = float(line[1])

  print("Loading basemap...")
  #with fiona.open(shapefilename+'.shp') as shp:
  #  coords = shp.bounds

  full_map = [-74.2555913638106, 40.49611539521161, -73.7000090638712, 40.91553277600008]
  manhattan_map = [-74.0555913638106, 40.69582408560584, -73.9000090638712, 40.88553277600008]
  coords = manhattan_map

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

  print("Building dataframe from map")
  df_map = pd.DataFrame({
        'poly': [Polygon(blocks) for blocks in m.nyc],
        'median_age': [tract_to_median.get(x["boro_code"] + x["ct2010"],0) for x in m.nyc_info],
        #'median_age': [block_to_median.get(x["bctcb2010"],0) for x in m.nyc_info],
        'block':[x["bctcb2010"] for x in m.nyc_info],
        'tract':[x["boro_code"] + x["ct2010"] for x in m.nyc_info]})
  filtered_df_map = pd.DataFrame(df_map[df_map["tract"].apply(lambda x:x[0]) == "1"])
  df_map = filtered_df_map
  print(df_map.head())

  print("Building image")
  figwidth = 14
  fig = plt.figure(figsize=(figwidth, figwidth*h/w))
  ax = fig.add_subplot(111, axisbg='w', frame_on=False)
  cmap = plt.get_cmap('Blues')
  #cmap = plt.get_cmap('hsv')
  #cmap = plt.get_cmap('gist_rainbow')

  # draw neighborhoods with grey outlines
  df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(x, ec='#111111', lw=.8, alpha=.6, zorder=4))
  pc = PatchCollection(df_map['patches'], match_original=True)

  all_tracts = sorted(list(set(df_map.tract)))
  minage_non0 = df_map[df_map["median_age"] > 0]["median_age"].min()*.75
  maxage = df_map["median_age"].max()
  
  minage_non0 = 24.75
  maxage = 48.0

  print("Min and Max Age: [%s,%s]"%(minage_non0,maxage))
  cmap_list = [x for x in df_map.median_age.apply(lambda x: (0,0,0,0) if x == 0 else cmap((x * 1.0 - minage_non0)/(maxage-minage_non0)))] 
  #cmap_list = [cmap(max(0, min(1,val))) for val in (df_map.median_age.values - 0)/65]
  #cmap_list = [cmap(x*1.0/len(all_tracts)) for x in df_map.tract.apply(lambda y:all_tracts.index(y))]
  pc.set_facecolor(cmap_list)
  ax.add_collection(pc)
  m.drawmapboundary(ax=ax, zorder=5)

  fig.suptitle(title, fontdict={'size':24, 'fontweight':'bold'}, y=0.92)
  #plt.show()
  plt.savefig(output_name, dpi=100, frameon=False, bbox_inches='tight', pad_inches=0.5, facecolor='#F2F2F2')

for [basename, output_name, title] in input_data:
  print("Building for %s"%output_name)
  build_choloropath(basename, output_name, title)
