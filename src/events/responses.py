from utils.utils import generate_number

def handle_response(message) -> str:

	p_message = message.lower().split(' ')

	if '!dado' in p_message or '!reroll' in p_message:
		return f':game_die: = {generate_number()}'

	if '!dobles' in p_message:
		return f':game_die: = {generate_number()}/{generate_number()}'




