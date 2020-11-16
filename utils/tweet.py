import aiohttp
from aiohttp.client import ClientSession
import aiohttp_oauth_client 
from authlib.client.aiohttp import AsyncOAuth1Client, OAuthRequest
import configs.twitter as twitter
import discord
from datetime import date, datetime

class Tweet:

    def __init__(self):
        pass

    async def tweet(self, sentence :str):
        """
        Tweet something.
        """

        post_url = "https://api.twitter.com/1.1/statuses/update.json"

        async with ClientSession(request_class=OAuthRequest) as session:
            client = AsyncOAuth1Client(
                session=session,
                client_id=twitter.CONSUMER_KEY,
                client_secret=twitter.CONSUMER_SECRET,
                token=twitter.ACCESS_TOKEN,
                token_secret=twitter.ACCESS_TOKEN_SECRET
                )
            
            params = {"status":sentence}

            tes = await client.post(
                url=post_url,
                data=params
                )
            print(tes)

    def replace_variable(self, sentence: str, owner: discord.User, activity: str ='None', status: str ='None'):
        time = datetime.now()
        vars_dict = {
            '(owner)': str(owner),
            '(owner_name)': owner.name,
            '(owner_discriminator)': str(owner.discriminator),
            '(owner_id)': str(owner.id),
            '(status)': status,
            '(activity)': activity,
            '(time)': f"{time.hour}:{time.second}",
            '(time_month_and_day)': f"{time.month}/{time.day}",
            '(time_year)': str(time.year),
            '(time_month)': str(time.month),
            '(time_day)': str(time.day),
            '(time_hour)': str(time.hour),
            '(time_minute)': str(time.minute),
            '(time_second)': str(time.second)
        }

        for before, after in vars_dict.items():
            sentence = sentence.replace(before, after)

        return sentence

