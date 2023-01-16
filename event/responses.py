import random

def generate_number() -> str:
	
	random_number = str(random.randint(0, 99))

	if len(random_number) == 1:
		return f'0{random_number}' 

	return random_number


def handle_response(message) -> str:

	p_message = message.lower().split(' ')

	if '!dado' in p_message or '!reroll' in p_message:
		return f':game_die: = {generate_number()}'

	if '!dobles' in p_message:
		return f':game_die: = {generate_number()}/{generate_number()}'
