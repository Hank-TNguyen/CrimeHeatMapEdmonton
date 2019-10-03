import sys
import sqlite3
import csv

try:
	with open(sys.argv[1]) as data: 
	
		reader = csv.reader(data, delimiter=',')
		conn = sqlite3.connect('data.db')
		c = conn.cursor()

		for row in reader:
			key_nbh = row[0].replace(' ', '_').replace("'", "").replace('"', '"')
			bind_this = (key_nbh, row[1], row[2], row[3][1:], row[4], row[5])			
			c.execute("insert into crime_data values(?, ?, ?, ?, ?, ?)", bind_this)

		conn.commit()
		conn.close()

except IndexError: 
	print("Params missing")

