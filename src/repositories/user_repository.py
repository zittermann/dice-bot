
def find(db, username):
	collection = db.users
	return collection.find_one({
		"username": username
	})

def create(db, username):

	collection = db.users
	total_users = collection.count_documents({})

	# I refuse using classes a for this bitch ass project 
	new_user = {
		"_id": total_users,
		"username": username,
		"latest": None,
		"record": 0,
		"consecutively": 0
	}

	collection.insert_one(new_user)

	return new_user

def update(db, updated_user):

	collection = db.users

	collection.find_one_and_update({
		"username": updated_user["username"]
	}, {"$set": updated_user})	
