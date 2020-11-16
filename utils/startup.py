from configs.token import TOKEN
import discord
from discord.ext import commands
from utils import StartupError, Check as check
import os

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

    def get_token(self) -> str:
        """
        Get token.
        """

        try:
            token = os.environ["TOKEN"]
        except:
            pass

        if not token:
            
            try:
                import configs.token
                token = configs.token.TOKEN
                if len(token) == 0:
                    raise StartupError('Activity bot token was not found.')
            
            except:
                raise StartupError('Activity bot token was not found.')

