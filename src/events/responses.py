from utils.utils import generate_number, number_to_emote
from services import user_service
from assets import emotes as e

def handle_response(username, message, mention) -> str:

	p_message = message.lower().split(' ')

	if '!dado' in p_message or '!reroll' in p_message:
		return f':game_die: = {generate_number()}'

	if '!dobles' in p_message:
		return f':game_die: = {generate_number()}/{generate_number()}'

	if '!register' in p_message:
		return user_service.register(username, mention)

	if '!came' in p_message:

		user_info, err = user_service.came(username, mention)
		if err is not None: # Golang developer experience 
			return err

		return handle_came(user_info, mention)

	if '!log' in p_message:
		return user_service.log(username)

 
# A lot of text warning! 
def handle_user_unregistered(mention) -> str:
	return f'''No jodas {mention} ni siquiera estás registrado en \
		la CC y ya te querés agarrar a mano cambiada {e.CHEEMS}.
		\nUsá el comando `!register` primero y dejate de joder'''

def handle_came(user_info, mention):
	
	record = user_info["record"]
	sequence = user_info["consecutively"]

	record_emotes = number_to_emote(record)
	sequence_emotes = number_to_emote(sequence)

	message = (f'''Hey {mention}! que sorpresa para '''
	'''nadie verte por acá otra vez.\n'''
	f'''Te recuerdo que tu mayor record de tremendas pajas consecutivas es de {record_emotes}. ''')


	if sequence == 1:
		message += (f'''\nEsta también es inicio de tu nueva vida como coomer promedio. Así es como comienza tu meteórica carrea hacia '''
		f'''el fracaso del coomer promedio {e.OK_ZOOMER}''')

	elif record > sequence:
		message += (f'''Pero como sos incapaz de mantener la constancia en algo'''
		f'''hasta ahora llevás {sequence_emotes} y contando. {e.NO_IDEA}''')

	elif sequence == record:
		message += (f'''\nY para sorpresa de nadie, sos tan pajín que {sequence_emotes} '''
		f'''también es la cantidad de pajas llevás consecutivas hasta ahora {e.PEKO}. '''
		f'''Sigue así, negro, total la adicción a la pornografía es un mito {e.COOMER}''')


	else:
		message = f"Cómo hiciste eso? {e.POCHITA}"

	return message
