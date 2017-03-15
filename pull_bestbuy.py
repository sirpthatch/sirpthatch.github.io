import os, sys, csv
import urllib.parse
import json, requests
from requests.exceptions import RequestException
import argparse, time
from datetime import datetime
from contextlib import closing
import zipfile
import itertools

API_KEY="sKde149XdQM3SynYU6AAFaMp"
MAX_RESULTS_PER_REQUEST=100

class CursorMarkQuery(object):
  def __init__(self, query, pause_seconds=0.5):
    self.query = query
    self.pause_seconds = pause_seconds

  def results(self, results_handler):
    next_query = self.query+"&cursorMark=*"
    errors = 0
    while(next_query):
      print("Querying: %s"%next_query)
      response = requests.get(next_query)
      try:
        response.raise_for_status()
        errors = 0
        json_response = response.json()

        if "nextCursorMark" in json_response and json_response["nextCursorMark"] != "":
          new_next_query = self.query + "&cursorMark=%s"%urllib.parse.quote_plus(json_response["nextCursorMark"])
          if next_query == new_next_query:
            next_query = None
          else: next_query = new_next_query
        else:
          next_query = None
        
        yield results_handler(json_response)
      except RequestException as r:
        errors += 1
        if errors > 3:
          raise Exception("Too many errors for query %s"%next_query)

      time.sleep(self.pause_seconds)

def flatten(nested_results):
  for f in nested_results:
    for m in f:
      yield m

def do_categories_pull(output):
  now = datetime.now()
  categories_api_endpoint = "https://api.bestbuy.com/v1/categories?format=json&apiKey=%s&show=all&pageSize=%s"%(API_KEY, MAX_RESULTS_PER_REQUEST)
  query = CursorMarkQuery(categories_api_endpoint)
  
  results = flatten(query.results(lambda x:x["categories"]))
  raw_output_file = os.path.join(output, now.strftime("%Y/%m/%d/%H%M%S/categories.jpl"))
  if not os.path.exists(os.path.dirname(raw_output_file)):
    os.makedirs(os.path.dirname(raw_output_file))

  with open(raw_output_file, "w") as w_handle:
    for res in results:
      w_handle.write(json.dumps(res)+"\n")

def do_stores_pull(output):
  now = datetime.now()
  stores_api_endpoint = "https://api.bestbuy.com/v1/stores?format=json&apiKey=%s&show=all&pageSize=%s"%(API_KEY, MAX_RESULTS_PER_REQUEST)
  query = CursorMarkQuery(stores_api_endpoint)
  
  results = flatten(query.results(lambda x: x["stores"]))
  raw_output_file = os.path.join(output, now.strftime("%Y/%m/%d/%H%M%S/stores.jpl"))
  if not os.path.exists(os.path.dirname(raw_output_file)):
    os.makedirs(os.path.dirname(raw_output_file))

  with open(raw_output_file, "w") as w_handle:
    for res in results:
      w_handle.write(json.dumps(res)+"\n")

def do_full_products_pull(output):
  now = datetime.now()
  endpoint = "https://api.bestbuy.com/v1/products.json.zip/?apiKey=%s"%API_KEY
  output_dir =  os.path.join(output, now.strftime("%Y/%m/%d/%H%M%S/"))
  output_file = os.path.join(output, output_dir,"work", "products.json.zip")
  if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))

  with closing(requests.get(endpoint, stream=True)) as response:
    with open(output_file, "wb") as w_handle:
      for chunk in response.iter_content(chunk_size=1024):
        w_handle.write(chunk)

  with zipfile.ZipFile(output_file, 'r') as zip_ref:
    zip_ref.extractall(os.path.join(output_dir, "work"))

  with open(os.path.join(output_dir, "products.checkpoint.jpl"), "w") as w_handle:
    for json_file in os.listdir(os.path.join(output_dir, "work")):
      if json_file.endswith(".json"):
        with open(os.path.join(output_dir, "work", json_file)) as handle:
          j_data = json.load(handle)
          for d in j_data:
            w_handle.write(json.dumps(d)+"\n")

def do_updated_products_pull(output):
  now = datetime.now()
  products_api_endpoint = "https://api.bestbuy.com/v1/products(itemUpdateDate>=today)?format=json&apiKey=%s&show=all&pageSize=%s"%(API_KEY, MAX_RESULTS_PER_REQUEST)
  query = CursorMarkQuery(products_api_endpoint)
  
  results = flatten(query.results(lambda x: x["products"]))
  output_file = os.path.join(output, now.strftime("%Y/%m/%d/%H%M%S/products.jpl"))
  if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))

  with open(output_file, "w") as w_handle:
    for res in results:
      w_handle.write(json.dumps(res)+"\n")

MAXIMUM_AVAILABILITY_PULL_SIZE = 60 # queries for more than this result in an error
MAXIMUM_AVAILABILITY_PAGE_SIZE = 10 # maximum page size for availability is lower than other endpoints
def do_products_availability_pull(output):
  now = datetime.now()
  checkpoint_files = []
  for root, dirs, files in os.walk(output):
    checkpoint_files.extend([os.path.join(root, f) for f in files if f.endswith("checkpoint.jpl")])

  latest_checkpoint_file = sorted(checkpoint_files)[-1]
  print("Searching for product skus...")
  def fetch_product_skus(checkpoint_file):
    with open(checkpoint_file) as handle:
      for line in handle:
        j_data = json.loads(line)
        yield j_data["sku"]

  all_product_skus = fetch_product_skus(latest_checkpoint_file)
  print("Building queries...")
  def build_queries(product_skus):
    while(True):
      skus_to_pull = list(itertools.islice(product_skus, MAXIMUM_AVAILABILITY_PULL_SIZE))
      if len(skus_to_pull) == 0:
        break
      sku_filter = "|".join(["sku="+str(n) for n in skus_to_pull])
      yield "https://api.bestbuy.com/v1/stores(area(39.8333,-98.5833,2000mi))+products(%s)?format=json&apiKey=%s&show=all&pageSize=%s"%(sku_filter, API_KEY, MAXIMUM_AVAILABILITY_PAGE_SIZE)
 
  queries = build_queries(all_product_skus)
  
  output_file = os.path.join(output, now.strftime("%Y/%m/%d/%H%M%S/availability.jpl"))
  if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))
  
  with open(output_file, "w") as w_handle:
    idx = 0
    for query in queries:
      cursor_query = CursorMarkQuery(query)
      results = flatten(cursor_query.results(lambda x:x["stores"]))
      for result in results:
        w_handle.write(json.dumps(result)+"\n")
      idx += 1
      print("%s queries finished, %s skus pulled..."%(idx, idx * MAXIMUM_AVAILABILITY_PULL_SIZE))
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser("Script to pull data from the Best Buy API")
  parser.add_argument("--endpoint", type=str, required=True, help="the endpoint to pull")
  parser.add_argument("--checkpoint", help="do a full pull, instead of just updates", action="store_true")
  parser.add_argument("--output", type=str, required=True, help="root output directory")

  args = parser.parse_args()
  
  def products_handler(output):
    if args.checkpoint:
      do_full_products_pull(output)
    else:
      do_updated_products_pull(output)

  endpoint_handlers = {
      "categories":do_categories_pull,
      "stores":do_stores_pull,
      "products":products_handler,
      "availability": do_products_availability_pull
      }

  if args.endpoint.lower() not in endpoint_handlers:
    raise Exception("Invalid endpoint, must be in %s"%(",".join(endpoint_handlers.keys())))

  print("Starting API calls..")
  endpoint_handlers[args.endpoint.lower()](args.output)
  print("Finished")

