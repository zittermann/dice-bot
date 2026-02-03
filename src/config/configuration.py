from dotenv import load_dotenv
import os

def load():

	stream = open('config.yml', 'r')
	dict = yaml.full_load(stream)

	return dict

def get_token():
	load_dotenv()
	return os.getenv("DISCORD_TOKEN")
