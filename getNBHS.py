import sys
import csv
import json

neighbourhoods = set()

def reportNeighbourhoods(nbhs, writeToFile):
	print("------------- REPORT -------------")
	print("There are " + str(len(nbhs)) + " nbh")
	if writeToFile:
		print("write to file: " + writeToFile)
	print("-------------- END ---------------")


try:
	with open(sys.argv[1]) as data: 
		reader = csv.reader(data, delimiter=',')
		for row in reader: 
			neighbourhoods.add(row[0])

		with open(sys.argv[2], 'w') as toFile:
			json.dump(list(neighbourhoods), toFile)

	
	reportNeighbourhoods(neighbourhoods, sys.argv[2])
except IndexError: 
	print("Params missing")

