from repositories import user_repository as users
from utils import utils
from database.connection import create_connection
from assets import emotes as e
import discord

FORMAT = '%Y-%m-%d'
DB = create_connection()

def find(username):
	return users.find(DB, username)

def register(username, mention):

	user = find(username)

	if user is not None:
		return f'Sague {mention}. Ya estás registrado, no hagas trampa {e.RAGE}'

	users.create(DB, username)
	return f'Me alegra informar que {mention} se ha unido a la Coomer Community {e.XD}'

# i didn't want to use classes for such a small project but
# probably should have, at least for the user logic :^(
# guess i'm paying for my sins
def came(username, mention):

	user = find(username)

	# iS THis a GolANg momentum?!!??!11
	# User does not exists error
	if user is None:
		return None, (f'''No jodas {mention} ni siquiera estás registrado en'''
			f'''la CC y ya te querés agarrar a mano cambiada {e.CHEEMS}. \n\n'''
			'''Usá el comando `!register` primero y dejate de joder''') 

	# User already came today error
	if already_came(user):
		return None, f'''Puto coomer, ya cumpliste por hoy, vas a tener que esperar hasta mañana {e.RAGE}'''

	user["consecutively"] = update_consecutively(user)
	user["record"] = update_record(user)
	user["latest"] = utils.today()

	users.update(DB, user)

	# User did not come today yet
	return user, None

# Reminds user why he is here!
def log(username):

	user = find(username)

	if user is None:
		return (f'Negro, ni siquiera estás registrado y querés consultar tu historial? {e.SKULL}\n'
		f'Acordate de usar el comando `!register` para comenzar tu camino a la perdición {e.COOMER}')

	message = f'Imaginate querer consultar tu record de pajas {e.CHEEMS}\n'

	record_emote = utils.number_to_emote(user["record"])
	record_sequence = utils.number_to_emote(user["consecutively"])

	message += (f"`\tTu record actual es:` {record_emote}\n"
	f"`\tY tu racha hasta hora es:` {record_sequence}")

	return message

### All come below should be in a class file or something but i hate myself
def is_consecutive(user):
	return utils.yesterday() == user["latest"]

def update_consecutively(user):

	sequence = int(user["consecutively"])

	return sequence + 1 if is_consecutive(user) else 1

def is_new_record(user):
	return user["consecutively"] > user["record"]

def update_record(user):

	record = int(user["record"])

	return record + 1 if is_new_record(user) else record 

def already_came(user):

	latest = user["latest"]

	return latest == utils.today() # Know if the latest was today
