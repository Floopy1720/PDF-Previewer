from pdf import *
import discord
import requests
import os

client = discord.Client()

@client.event
async def on_ready():
	print('You have awaken me as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.attachments:
		if message.attachments[0].url.endswith('.pdf'):
			await message.channel.send('Processing The File Please Wait')
			pdf = message.attachments[0].url
			r = requests.get(pdf, stream = True)
			with open("file.pdf","wb") as pdf:
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						pdf.write(chunk)
			path = "file.pdf"
			pdf_splitter(path)
			img("file_done.pdf")
			await message.channel.purge(limit=1)
			#await message.channel.send(file=discord.File('file.jpg'))
			name = message.attachments[0].url
			name = name[77:]
			size = os.path.getsize("file.pdf")
			size = convert_size(size)
			image = discord.File("file.jpg")
			embed=discord.Embed(title="Sender", description=message.author)
			embed.set_author(name="PDF Preview")
			embed.add_field(name="File Name", value=name, inline=True)
			embed.add_field(name="FIle Size", value=size, inline=True)
			embed.set_image(url="attachment://file.jpg")
			embed.set_footer(text="Made By Floppy#6269")
			await message.channel.send(file= image,embed=embed)


client.run('Your Token')