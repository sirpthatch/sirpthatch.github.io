import feedparser
import os, sys, csv,json
import argparse
from datetime import datetime

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='App to pull down the headlines from a collection of RSS feeds')

  parser.add_argument('--subscriptions', type=str, required=True, help="the subscription files")
  parser.add_argument('--output', type=str, required=True, help="the output directory")

  args = parser.parse_args()
  
  today = datetime.now().strftime("%Y%m%d")

  urls = dict()
  with open(args.subscriptions) as handle:
    reader = csv.reader(handle)
    for line in reader:
      [name, url, parse_summary] = line
      urls[name] = (url, parse_summary == "True")

  fields = ["link","title","summary"]
  for name,(url, parse_summary) in urls.items():
    print("Parsing %s, from %s, parsing summary:%s"%(name, url, parse_summary))
    feed = feedparser.parse(url)
    entries = []
    
    for entry in feed["entries"]:
      data = dict((x, entry[x]) for x in fields)
    
      if not parse_summary:
        data["summary"] = ""

      entries.append(data)

    output_file = os.path.join(args.output, today+"."+name+".json")
    with open(output_file,"w") as w_handle:
      json.dump(entries, w_handle)





  
