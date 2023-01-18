import random
from datetime import datetime

def generate_number() -> str:
	
	random_number = str(random.randint(0, 99))

	if len(random_number) == 1:
		return f'0{random_number}' 

	return random_number

def today():
	return datetime.now().strftime('%Y-%m-%d')
