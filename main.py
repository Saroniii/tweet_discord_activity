# coding: UTF-8
import discord
from discord.ext import commands

import configs.twitter as twitter
import configs.token as token
from utils import Tweet as tweet
from utils import CogLoader as loader
from utils import Check as check
import configs.twitter as config

TOKEN = token.TOKEN #TOKEN load from token.py
command_prefix = ['!'] #Prefix

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.ready_check = False  # Variable to prevent duplicate on_ready events from being triggered
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        owner = await check().get_bot_owner(self)
        await check().can_startup(owner=owner, bot=self)
        if self.ready_check == False:

            print('Logged in as')
            print(self.user.name)
            print(self.user.id)
            print(f'import')
            folder_name = 'cogs'
            loader().cog_load(self, f'{folder_name}/*.py')

            print('------')
            self.ready_check = True
            self.lang = twitter.LANG
            self.owner = owner
        else:
            print('The start up process is already complete!')

#This bot will use presence intent and members intent.
intent: discord.Intents = discord.Intents.all()
bot = MyBot(command_prefix=command_prefix, intents=intent)

bot.run(TOKEN)
