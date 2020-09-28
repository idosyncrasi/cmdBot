import discord

client = discord.Client()

@client.event
async def on_ready():
	print('Logged on as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == 'cmdBot#5426':
		return
	await ping(message)
	await commands(message)
	await sus(message)
	await bot(message)
	await cjs(message)
	await sad(message)

async def ping(message):
	mess = message.content
	if mess == 'ping':
		await message.channel.send('pong')
	elif mess == 'Ping':
		await message.channel.send('Pong')
	elif mess == 'PING':
		await message.channel.send('PONG')
	elif mess == '*ping*':
		await message.channel.send('*pong*')
	elif mess == '**ping**':
		await message.channel.send('**pong**')

async def commands(message):
	mess = message.content
	prefix = '!'
	if not mess.startswith(prefix):
		return
	if not message.author.guild_permissions.value == 2147483647:
		await message.channel.send("You don't have permission to use this. Go away.")
		return
	cmd = mess[1:][:mess[1:].find(' ')]
	args = mess[1:][mess[1:].find(' ')+1:].split(' ')
	if cmd == 'help':
		await message.channel.send("Usage: [cmd] [arg]...")
		await message.channel.send("help: print this help")
		await message.channel.send("mute: mute a vc")
		await message.channel.send("unmute: unmute a vc")
	elif cmd == 'mute':
		if len(args) == 2:
			chnl = args[0]
			act = args[1]
			if act == 'all':
				for chnnl in message.guild.channels:
					if chnnl.name == chnl:
						for mem in chnnl.members:
							try:
								await mem.edit(mute=True)
							except discord.errors.HTTPException:
								pass
			else:
				for chnnl in message.guild.channels:
					if chnnl.name == chnl:
						for mem in chnnl.members:
							name = mem.name
							if name == act:
								try:
									await mem.edit(mute=True)
								except discord.errors.HTTPException:
									pass

		else:
			await message.channel.send("Usage: mute [channel] [action]")
			await message.channel.send("Channel: any vc channel")
			await message.channel.send("Action: all/specific user")
	elif cmd == 'unmute':
		if len(args) == 2:
			chnl = args[0]
			act = args[1]
			if act == 'all':
				for chnnl in message.guild.channels:
					if chnnl.name == chnl:
						for mem in chnnl.members:
							try:
								await mem.edit(mute=False)
							except discord.errors.HTTPException:
								pass
			else:
				for chnnl in message.guild.channels:
					if chnnl.name == chnl:
						for mem in chnnl.members:
							name = mem.name
							if name == act:
								try:
									await mem.edit(mute=False)
								except discord.errors.HTTPException:
									pass
		else:
			await message.channel.send("Usage: unmute [channel] [action]")
			await message.channel.send("Channel: any vc channel")
			await message.channel.send("Action: all/specific user")
	else:
		await message.channel.send("Usage: [cmd] [arg]...")
		await message.channel.send("help: print this help")
		await message.channel.send("mute: mute a vc")
		await message.channel.send("unmute: unmute a vc")

async def bot(message):
	mess = message.content
	if 'bot' in mess or 'BOT' in mess or 'Bot' in mess:
		if 'bad' in mess or 'mean' in mess or 'Bad' in mess or 'Mean' in mess:
			await message.channel.send(">:[")
		elif 'good' in mess or 'nice' in mess or 'best' in mess or 'Good' in mess or 'Nice' in mess or 'Best' in mess:
			await message.channel.send(":D")
		elif 'rip' in mess or 'RIP' in mess or 'Rip' in mess:
			await message.channel.send("D:")
		if 'cookie' in mess or 'kookie' in mess or 'koocie' in mess or ':cookie:' in mess or 'Cookie' in mess or 'Kookie' in mess or 'Koocie' in mess:
			await message.channel.send("Here's a :cookie:")

async def sad(message):
	mess = message.content
	if 'im sad' in mess or 'i am sad' in mess or 'I am sad' in mess or 'Im sad' in mess or "i'm sad" in mess or "I'm sad" in mess:
		await message.channel.send(message.author.mention + " *head pat*")

async def sus(message):
	mess = message.content
	if " sus" in mess or " SUS" in mess:
		mentioned = mess[ (mess.find('&')+1):mess.find('>') ]
		for role in message.guild.roles:
			if str(role.id) == mentioned:
				await message.channel.send(role.mention + " was ejected")

async def cjs(message):
	mess = message.content
	if ("jack sparrow" in mess or "Jack Sparrow" in mess or "Jack sparrow" in mess or "jack Sparrow" in mess) and not("captain" in mess or "Captain" in mess):
			await message.channel.send("That's Captain Jack Sparrow to you")


def main():
	client.run()

if __name__ == '__main__':
	main()
