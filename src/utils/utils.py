import random
from datetime import datetime, timedelta

def generate_number() -> str:
	
	random_number = str(random.randint(0, 99))

	if len(random_number) == 1:
		return f'0{random_number}' 

	return random_number

def today() -> datetime:
	return datetime.now()

def yesterday() -> str:
	return today() - timedelta(1).strftime('%Y-%m-%d')