import sys
import sqlite3
import json

try:
	# with open(sys.argv[1]) as data: 
	with open('nbhs.json') as data: 
		nbhs = json.load(data)
		conn = sqlite3.connect('data.db')
		c = conn.cursor()

		for nbh in nbhs:
			key_nbh = nbh.replace(' ', '_').replace("'", "").replace('"', '"')
			c.execute("insert into mapKeyNBH values(?, ?)", (nbh, key_nbh))

		conn.commit()
		conn.close()

except IndexError: 
	print("Params missing")

