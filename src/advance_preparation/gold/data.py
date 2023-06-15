import json
import csv
import re

def include_key(date_keys, key):
  if(key in date_keys):
    return 1
  else:
    return 0

# 金価格情報
with open('./gold.json') as f:
    gold = json.load(f)
data = gold['gold']

date = list(data.keys())
date.sort()

# NASDAQ 情報
with open('./nasdaq.csv', encoding='utf8', newline='') as f:
    next(csv.reader(f))
    csvreader = csv.reader(f)
    for row in csvreader:
        key_date = row[0].split('/')
        key = key_date[0] + key_date[1].zfill(2) + key_date[2].zfill(2)
        if(key in date):
            data[key]['nasdaq_start'] = float(re.sub(',', '', row[2]))
            data[key]['nasdaq_end'] = float(re.sub(',', '', row[1]))
            data[key]['price'] = float(re.sub(',', '', data[key]['price']))

## ファイル出力
csv_path = r"../../output/gold.csv"

with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date', 'gold_price', 'gold_diff', 'gold_diff_percent', 'nasdaq_start', 'nasdaq_end'])

    for ymd in date:
        date_value = data[ymd]
        data_keys = list(date_value.keys())
        if 0 == include_key(data_keys, 'nasdaq_start') or 0 ==  include_key(data_keys, 'nasdaq_end'):
            continue
        writer.writerow([
          ymd,
          date_value['price'],
          date_value['diff'],
          date_value['diff_percent'],
          date_value['nasdaq_start'],
          date_value['nasdaq_end']
      ])
