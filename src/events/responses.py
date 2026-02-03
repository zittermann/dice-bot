from utils.utils import generate_number, number_to_emote
from assets import emotes as e

def handle_response(username, message, mention) -> str:

	p_message = message.lower().split(' ')

	if '!dado' in p_message or '!reroll' in p_message:
		return f':game_die: = {generate_number()}'

	if '!dobles' in p_message:
		return f':game_die: = {generate_number()}/{generate_number()}'
