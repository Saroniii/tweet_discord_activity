import pathlib
from discord.ext import commands


class CogLoader:

    def cog_load(self, bot :commands.Bot, path: str):
        """
        Load cogs.
        """
        cur = pathlib.Path('.')

        for p in cur.glob(path):

            try:
                print(f'cogs.{p.stem}', end="　")
                bot.load_extension(f'cogs.{p.stem}')
                print(f'success')

            except commands.errors.NoEntryPointError:
                print(f'module.{p.stem}')
