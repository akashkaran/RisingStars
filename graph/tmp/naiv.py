import csv
import sys
import json

fieldnames=["name","icc","naive"]

def convert(result):
  csv_filename = "result1.csv"
  print ("Opening CSV file: "+csv_filename)
  f=open(csv_filename, 'r')
  csv_reader = csv.DictReader(f,fieldnames)
  json_filename = csv_filename.split(".")[0]+".js"
  print("Saving JSON to file: "+json_filename)
  jsonf = open(json_filename,'w')
  stvar="var jsonfile={jsonarray:"
  end="};"
  data = json.dumps([r for r in csv_reader])
  jsonf.write(stvar)
  jsonf.write(data)
  jsonf.write(end)
  f.close()
  jsonf.close()

if __name__=="__main__":
    convert(sys.argv[1:])
