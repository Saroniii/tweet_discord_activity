import discord
from discord.ext import commands
from utils import StartupError, Check as check

class Startup:

    def __init__(self):
        self.check = check()

    async def setup(self, bot :commands.Bot):
        """
        Startup the bot.
        """
        
        owner = await self.check.get_bot_owner(bot)
        startup_check = await self.check.can_startup(owner, bot)

        if not startup_check[0]:
            raise StartupError(startup_check[1])

        return owner
