import os, sys
import pandas as pd
from datetime import datetime

input_file = "/Volumes/Trunk/Data/citibike/citibike-tripdata-final-fips-date-age.csv"
output_directory = "/Volumes/Trunk/Data/citibike/daypart_analysis/"

if not os.path.exists(output_directory):
  os.makedirs(output_directory)

def fips_to_tract(fips):
  return str(fips)[4:11]

frame = pd.read_csv(input_file)
frame["Start_Tract"] = frame["start_fips"].apply(fips_to_tract)

print("Computing the overall median age by tract")
frame.groupby("Start_Tract").Age.median().to_csv(os.path.join(output_directory, "medianage.tract.csv"))

print("Computing median age by date")
frame.groupby("Date").Age.median().to_csv(os.path.join(output_directory, "date_to_median_age.csv"))

print("Computing total trip duration by date")
frame.groupby("Date").tripduration.sum().to_csv(os.path.join(output_directory, "date_to_duration.csv"))

print("Computing total number of trips by date")
frame.groupby("Date").tripduration.count().to_csv(os.path.join(output_directory, "date_to_num_trips.csv"))

def bucket_hour(hour):
  try:
    hour_int = int(hour)
    if (hour < 5): return "night"
    if (hour < 10): return "earlymorning"
    if (hour < 12): return "morning"
    if (hour < 16): return "afternoon"
    if (hour < 20): return "evening"
    else: return "night"
  except ValueError: return None

def weekday_checker(datestr):
  try:
    date = datetime.strptime(str(int(datestr)), "%Y%m%d")
    return date.weekday() < 5
  except ValueError: return None


frame["Hour_Bucket"] = frame["Hour"].apply(bucket_hour)
frame["Is_Weekday"] = frame["Date"].apply(weekday_checker)

print("Computing the average age by daypart")
frame.groupby("Hour_Bucket").Age.median().to_csv(os.path.join(output_directory, "medianage.hourbucket.csv"))

weekday_rides = frame[frame["Is_Weekday"] == True]
weekend_rides = frame[frame["Is_Weekday"] == False]

print("Computing weekday versus weekend median ages by geography")
weekday_rides.groupby("Start_Tract").Age.median().to_csv(os.path.join(output_directory,"medianage.weekday.tract.csv"))
weekend_rides.groupby("Start_Tract").Age.median().to_csv(os.path.join(output_directory,"medianage.weekend.tract.csv"))

print("Computing weekday versus weekend median age by geography and hour bucket")
for hour_bucket, data in weekday_rides.groupby("Hour_Bucket"):
  data.groupby("Start_Tract").Age.median().to_csv(os.path.join(output_directory, "medianage.weekeday.%s.tract.csv"%hour_bucket))

for hour_bucket, data in weekend_rides.groupby("Hour_Bucket"):
  data.groupby("Start_Tract").Age.median().to_csv(os.path.join(output_directory, "medianage.weekeend.%s.tract.csv"%hour_bucket))

