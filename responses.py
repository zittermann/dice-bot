import random

def handle_response(message) -> str:

	p_message = message.lower()
	random_number = str(random.randint(0, 99))

	if p_message == 'dado':
		return f':game_die: = {random_number}'
