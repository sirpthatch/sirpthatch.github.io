import os, sys, csv,json
import argparse
import nltk
from datetime import datetime

PROPER_NOUN_TAGS = set(["NNP","NNPS"])
NOUN_TAGS = PROPER_NOUN_TAGS.union(set(["NN","NNS"]))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='App to extract some data out of the RSS feed data')

  parser.add_argument("--input", type=str, required=True, help="the input directory")
  parser.add_argument('--date',   type=str, default=datetime.now().strftime("%Y%m%d"), required=False, help="the subscription files")
  parser.add_argument('--output', type=str, required=True, help="the output directory")

  args = parser.parse_args()

  files_to_process = [x for x in os.listdir(args.input) if x.startswith(args.date)]
  for f in files_to_process:
    input_file = os.path.join(args.input, f)
    output_file = os.path.join(args.output, f)
    
    data = None
    with open(input_file) as handle:
      data = json.load(handle)

    processed_data = []
    for entry in data:
      nouns = []
      proper_nouns = []
      simple_title = entry["title"].replace("'","").replace('"','')
      simple_summary = entry["summary"].replace("'","").replace('"','')
      tree = nltk.chunk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(simple_title + ".  "+simple_summary)))
      for part in tree.pos():
        [[word, tag], label] = part
        if tag in PROPER_NOUN_TAGS: proper_nouns.append(word)
        if tag in NOUN_TAGS: nouns.append(word)
      entry["nouns"] = list(set(nouns))
      entry["proper_nouns"] = list(set(proper_nouns))
      processed_data.append(entry)
    
    with open(output_file,"w") as w_handle:
      json.dump(processed_data,w_handle)
