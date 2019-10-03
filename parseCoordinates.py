import sys
import csv
import json

def process_response(nbh, res):
	if (res['status'] != "OK"):
		print("XXXX Bad response" + res['status'])
		return
	
	result = res['results'][0]
	# print(nbh)
	loc = result['geometry']['location']
	with open("coordinates.dat", 'a') as writeFile: 
		writer = csv.writer(writeFile, delimiter='|')
		writer.writerow([nbh, loc['lat'], loc['lng']])
		

try:
	path = sys.argv[1].replace('"', '').replace("'", "")

	with open(path) as data: 
		nbh_res = json.load(data)
		process_response(path[path.index('/', 3) + 1:], nbh_res)
except IndexError: 
	print("Params missing")
