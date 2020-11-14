import discord
from discord.ext import commands
from utils import GetActivity as get_activity, Tweet as tweet
import configs.twitter as config


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.get_activity = get_activity()
        self.tweet = tweet()

    @commands.Cog.listener()
    async def on_member_update(self, before :discord.Member, after :discord.Member):
        
        try:
            if not before == self.bot.owner:
                return
            
            check_list = [
                [before.status, after.status],
                [before.activity, after.activity],
            ]
            
            before_flag = None
            after_flag = None

            for check in check_list:

                if check[0] != check[1]:
                    before_flag = check[0]
                    after_flag = check[1]
                    break

            print(type(before_flag))
            print(type(after_flag))
            status_type = None
            activity_name = None
            status_name = None 
            sentence = None

            if type(before_flag) or type(after_flag) in [discord.Game, discord.Streaming, discord.CustomActivity]:
                
                if not before_flag or before_flag and after_flag is not None:
                    status_type = 'activity_start'
                    activity_name = after_flag.name
                
                elif not after_flag:
                    status_type = 'activity_end'
                    activity_name = before_flag.name
            
            elif type(before_flag) or type(after_flag) in [discord.Status, discord.enums._EnumValue_Status]:

                status_type = 'status'
                status_name = self.get_activity.get_status(after_flag, self.bot.lang)
    
            else:
                return

            if status_type == 'activity_start':
                
                sentence = self.tweet.replace_variable(
                    sentence=config.START_ACTIVITY_TWEET,
                    owner=self.bot.owner,
                    activity=activity_name,
                    )
            
            elif status_type == 'activity_end':
                
                sentence = self.tweet.replace_variable(
                    sentence=config.END_ACTIVITY_TWEET,
                    owner=self.bot.owner,
                    activity=activity_name,
                    )

            elif status_type == 'status':
                
                sentence = self.tweet.replace_variable(
                    sentence=config.CHANGE_STATUS_TWEET,
                    owner=self.bot.owner,
                    status=status_name,
                    )
            
            await self.tweet.tweet(sentence)
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Cog(bot))