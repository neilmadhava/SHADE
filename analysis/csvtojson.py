import csv
import json

csvfile = open('tweets.csv', 'r')
jsonfile = open('tweets.json', 'w')

fieldnames = ("text", )
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out + '\n')