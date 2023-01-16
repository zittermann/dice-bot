from database.configuration import load
from pymongo import MongoClient

def create_connection() -> str:

	# Get a map with config.yaml content
	database = load()['Database']
	database_name = database["name"] # Getting database name

	# Generating connection string
	conn_string = f'mongodb+srv://{database["user"]}:{database["password"]}@{database["host"]}/?retryWrites=true&w=majority'
	
	# Connection to db
	cluster = MongoClient(conn_string)
	db = cluster[database_name]

	return db
