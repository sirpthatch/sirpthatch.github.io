import os, sys, csv
import requests

input_file = "/Volumes/Trunk/Data/citibike/citibike-tripdata-final.csv"
output_file = "/Volumes/Trunk/Data/citibike/citibike-tripdata-final-fips.csv"

station_id_to_latlong = dict()
with open(input_file) as handle:
  reader = csv.reader(handle)
  next(reader)
  for line in reader:
    station_id_to_latlong[line[3]] = (line[5], line[6])

def build_request(lat,log):
  return "http://data.fcc.gov/api/block/find?format=json&latitude=%s&longitude=%s&showall=false"%(lat,log)

station_to_fips = dict()
for station_id, location in station_id_to_latlong.items():
  [lat,log] = location
  request_url = build_request(lat,log)
  try:
    data = requests.get(request_url).json()
    station_to_fips[station_id] = data["Block"]["FIPS"]
  except:
    print("Unable to process request for: %s"%request_url)

with open(input_file) as handle:
  reader = csv.reader(handle)
  header = next(reader) + ["start_fips", "end_fips"]
  with open(output_file, "w") as w_handle:
    writer = csv.writer(w_handle)
    writer.writerow(header)
    for line in reader:
      start_id = line[3]
      end_id = line[7]
      full_data = line + [station_to_fips.get(start_id,""), station_to_fips.get(end_id,"")]
      writer.writerow(full_data)


