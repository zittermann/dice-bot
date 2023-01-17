import base64, gridfs

def load_pic(db, pic, directory, count):

	fs = gridfs.GridFS(db)
	
	file_location = directory + pic
	filename = pic.decode("utf-8")
	
	with open(file_location, "rb") as img_file:
		encoded_string = base64.b64encode(img_file.read())

	
	file_id = fs.put(encoded_string, filename=filename)
	db.pics.insert_one({"_id": count, "filename": filename, "file_id": file_id})

######### GET AN IMAGE ##########

# file = fs.find_one({"filename": "Mash_Kyrielight_Fate.jpeg"})
# bytedata = file.read()

# img_IO = BytesIO(base64.b64decode(bytedata))
# img_PIL = Image.open(img_IO)
# img_PIL.show()
