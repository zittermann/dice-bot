import random

def handle_response(message) -> str:

	p_message = message.lower().split(' ')

	if p_message[0] == 'dado':
		random_number = str(random.randint(0, 99))
		return f':game_die: = {random_number}'

	if p_message[0] == 'dobles':
		first_random = str(random.randint(0, 99))
		second_random = str(random.randint(0, 99))
		return f':game_die: = {first_random}/{second_random}'
