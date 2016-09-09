import os, sys
import pandas as pd
from datetime import datetime

data_file = "citibike-tripdata-withcensus.csv"

DATE_FORMATS = ["%Y-%m-%d %H:%M:%S","%m/%d/%Y %H:%M:%S"]
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



frame["Date"] = frame.starttime.apply(lambda x:try_parse(x, "%Y%m%d"))
frame["Hour"] = frame.starttime.apply(lambda x:try_parse(x, "%H"))

frame.to_csv("citibike-tripdata-withcensus-daytime.csv")

