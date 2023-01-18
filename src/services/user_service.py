from repositories import user_repository as users
from src.utils import utils

FORMAT = '%Y-%m-%d'

def register_user(db, username):

	users.create(db, username)

def came(db, username):

	user = users.find(db, username)

	user["consecutively"] = update_consecutively(user)
	user["record"] = update_record(user)
	user["latest"] = utils.today()

	users.update(db, user)

def is_consecutive(user):
	return utils.yesterday() == user["latest"]

def is_new_record(user):
	return user["consecutively"] > user["record"]

def update_consecutively(user):

	sequence = int(user["consecutively"])

	return sequence + 1 if is_consecutive(user) else 0

def update_record(user):

	record = int(user["record"])

	return record + 1 if is_new_record(user) else record 
