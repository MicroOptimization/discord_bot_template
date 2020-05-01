"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import discord
import generic_key_retriever
import asyncio

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        self.text_channel_names = []
        self.text_channels = []
        
        for i in client.get_all_channels():
            self.text_channel_names.append(str(i))
            self.text_channels.append(i)
            
        await client.change_presence(activity=discord.Game(name="with <word>"))
    
    async def on_message(self, message):    
        print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
        text = message.content
        words = text.split(" ")
        
        
        id = 0 #Insert an ID int here
        
        await asyncio.sleep(0.5)
        await message.channel.send("'{}'".format("Hello there, I'm a bot"))
        
        
        #User_id comes from when you @ a user in a message that the bot detects.
        #user = client.get_user(int(user_id[2][3:-1]))
        #Allows you to DM another user if you use:
        #await user.send("Your Message")

client = MyClient()

key = generic_key_retriever.get_key() #Insert your key here

client.run(key)