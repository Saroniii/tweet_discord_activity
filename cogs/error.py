import discord
from discord.ext import commands
from utils import StartupError


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot :commands.Bot =bot


    @commands.Cog.listener()
    async def on_command_error(self, error):
        if type(error) == StartupError:
            print("Bot was raised startup error.\nBot will be disconnect from discordAPI.")
            await self.bot.close()


def setup(bot):
    bot.add_cog(Cog(bot))