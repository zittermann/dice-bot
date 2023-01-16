from event import bot
from database.connection import create_connection

if __name__ == '__main__':

	create_connection()

	bot.run_bot()
