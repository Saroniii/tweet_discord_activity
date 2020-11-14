import discord

class GetActivity:

    def __init__(self):
        pass

    def get_status(self, status :discord.Status, lang) -> str:
        """
        Return status word.
        """
        if lang == 'en' or not 'ja':
            if status == discord.Status.online:
                return 'online'

            elif status == discord.Status.idle:
                return 'idle'

            elif status == discord.Status.dnd:
                return 'dnd'
            
            else:
                return 'offline'
        elif lang == 'ja':
            if status == discord.Status.online:
                return 'オンライン'

            elif status == discord.Status.idle:
                return '退席中'

            elif status == discord.Status.dnd:
                return '取り込み中'
            
            else:
                return 'オフライン'