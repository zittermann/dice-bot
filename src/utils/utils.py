import random
from datetime import datetime, timedelta
from assets import emotes as e

def generate_number() -> str:
	
	random_number = str(random.randint(0, 99))

	if len(random_number) == 1:
		return f'0{random_number}' 

	return random_number


# the difference between now and today is that 
# today is converted to string  
def now() -> datetime:
	return datetime.now()

def today() -> str:
	return now().strftime('%Y-%m-%d')

# Use now instead of today so we can use math logic
# to generate the date of yesterday
def yesterday() -> str:
	return (now() - timedelta(1)).strftime('%Y-%m-%d')

# turn a number into its equivalents with discord emotes
def number_to_emote(number):

	emote = ""

	for i in iter(str(number)): # iter(str(number)) converts number to integer
		emote += e.NUMBERS[int(i)] # convert index to integer again so we can find it's emoji equivalent

	return emote
