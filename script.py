import os
from scripts import pics
from scripts import characters

# Takes directory, fsencode is to avoid problems with specials characters
DIRECTORY = os.fsencode('/home/zitter/workspace/dice-bot/data/')

def run_script(db):
	# Loop through every element in directory
	for pic in os.listdir(DIRECTORY):

		total_docs = db.pics.count_documents({})

		pics.load_pic(db=db, pic=pic, directory=DIRECTORY, count=total_docs)
		characters.load_character(db=db, pic=pic, count=total_docs)
