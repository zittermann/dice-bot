
def load_character(db, pic, count):
	
	# Convert byte string to string
	pic = pic.decode("utf-8")
	character_info = pic.split("_")

	# Create a new string with every element of the array except the last one
	name = " ".join(character_info[:-1])

	# Create a new string with every element of source array
	# Last element is ALWAYS source info
	source_info = character_info[-1].split("+")
	source = " ".join(source_info)
	
	db.characters.insert_one({"_id": count, "name": name, "source": source})
