import os, sys
import pandas as pd
from datetime import datetime

data_file = "/Volumes/Trunk/Data/citibike/citibike-tripdata-final-fips.csv"
output_file = "/Volumes/Trunk/Data/citibike/citibike-tripdata-final-fips-date-age.csv"

DATE_FORMATS = ["%Y-%m-%d %H:%M:%S","%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M"]
def parse_date(date_str):
  date = None
  for date_f  in DATE_FORMATS:
    try:
      date = datetime.strptime(date_str, date_f)
    except ValueError:
      pass
  return date

frame = pd.read_csv(data_file, parse_dates=["starttime","stoptime"], date_parser=parse_date)

def try_parse(x, format_str):
  try:
    return x.strftime(format_str)
  except ValueError:
    return None

def compute_age(year):
  if len(str(year)) == 4:
    return 2016 - int(year)
  else: return None

frame["Age"] = frame["birth year"].apply(compute_age)
frame["Date"] = frame.starttime.apply(lambda x:try_parse(x, "%Y%m%d"))
frame["Hour"] = frame.starttime.apply(lambda x:try_parse(x, "%H"))

frame.to_csv(output_file)

