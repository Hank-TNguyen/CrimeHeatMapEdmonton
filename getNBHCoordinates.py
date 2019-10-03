import sys
import json
import requests
import os
import urllib.parse

logging = True
saveResponse = True

def printf(args):
	if logging:
		print(">> " + args)

def geocoding_url_builder(address, apikey):
	return "https://maps.googleapis.com/maps/api/geocode/json?address=" + urllib.parse.quote(address) + "&key=" + apikey

def requestGoogleGeocoding(address, apikey_file):
	if saveResponse:
		try:
			os.mkdir("geocoding")
		except FileExistsError:
			pass

	with open(apikey_file) as apikey:
		key = apikey.read()

		url = geocoding_url_builder(address, key)
		printf(url)

		if saveResponse:
			response = requests.get(url)
			printf(str(response.json()))
			fileName = address[:address.index(',')]
			with open("geocoding/" + fileName, 'w') as writeFile: 
				json.dump(response.json(), writeFile)


try:
	with open(sys.argv[1]) as data: 
		loaded_data = json.load(data)
		# for nbh in loaded_data:
		# 	nbh += ", Edmonton, Alberta, Canada"
		# 	requestGoogleGeocoding(nbh, sys.argv[2])

		nbh = "River's Edge"
		nbh += ", Edmonton, Alberta, Canada"
		requestGoogleGeocoding(nbh, sys.argv[2])


except IndexError: 
	printf("Params missing")

