from events import bot
import src.scripts.script as script
from database.connection import create_connection

DB = create_connection()

if __name__ == '__main__':
	
	bot.run_bot()
	# script.run_script(DB)