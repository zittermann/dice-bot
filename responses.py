import random

def handle_response(message) -> str:

	p_message = message.lower().split(' ')

	if '!dado' in p_message or '!reroll' in p_message:
		random_number = str(random.randint(0, 99))
		return f':game_die: = {random_number}'

	if '!dobles' in p_message:
		first_random = str(random.randint(0, 99))
		second_random = str(random.randint(0, 99))
		return f':game_die: = {first_random}/{second_random}'
