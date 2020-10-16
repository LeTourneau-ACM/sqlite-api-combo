import sqlite3
from sqlite3 import Error
import requests
import json

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

def main():
	# # Send GET request to the API
	# raw_data = requests.get("https://catfact.ninja/facts?limit=50")

	# # Turn the raw data into a json format
	# json_data = json.loads(raw_data._content)

	# For the plebs on the lab computer we need to read from the json file
	with open('cat_facts.json', 'r') as input_file:
		data = input_file.read()
		json_data = json.loads(data)

	# Create the database connection
	database = "pythonsqlite.db"
	conn = create_connection(database)

	cur = conn.cursor()

	# Input the facts into the database
	for item in json_data["data"]:
		cur.execute("INSERT INTO Facts(fact) VALUES(\"" + item["fact"] + "\");")
		conn.commit()

	cur.execute("SELECT * FROM Facts;")
	temp = cur.fetchall()

	for fact in temp:
		print(fact)

if __name__ == "__main__":
	main()
