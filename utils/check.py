import os
from typing import Tuple
import discord
from discord.ext import commands

class Check:

    def __init__(self):
        pass

    async def get_bot_owner(self, bot :commands.Bot) -> discord.User:
        """
        Return bot owner.
        """
        appinfo :discord.AppInfo = await bot.application_info()
        return appinfo.owner

    async def can_startup(self, owner :discord.User, bot :commands.Bot) -> Tuple:
        """
        Check meet requirement for startup.
        """
        if len(bot.guilds) > 1 or len(bot.guilds) == 0:
            return False, "The activity detection Bot must be placed on a single server."

        members = await bot.guilds[0].fetch_members(limit=None).flatten()

        if not owner in members:
            return False, "Bot owner must member of check activity server."

        if bot.intents != discord.Intents.all():
            return False, "Bot intents must be enable all."

        if not os.path.isfile('configs/twitter.py'):
            return False, "Activity bot can't found twitter data file."

        return True, "Startup check is success."
        
    

