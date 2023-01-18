import discord, os
from events import responses
from dotenv import load_dotenv

load_dotenv()

async def send_message(message, user_message):
	
	try:

		response = responses.handle_response(user_message)

		await message.reply(response)

	except Exception as e:
		print(e)


def run_bot():

	intents = discord.Intents.all()
	client = discord.Client(intents=intents)

	@client.event
	async def on_ready():
		print(f"{client.user} is now running!")

	@client.event
	async def on_message(message):

		# Prevents infinite loops
		if message.author == client.user:
			return  

		user_message = str(message.content)
		
		if '!' in user_message:
			await send_message(message, user_message)

	client.run(os.getenv('TOKEN'))
