import aiohttp
from aiohttp.client import ClientSession
import aiohttp_oauth_client 
from authlib.client.aiohttp import AsyncOAuth1Client, OAuthRequest
import configs.twitter as twitter

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
            
            params = {"status":"hello world"}

            await client.post(
                url=post_url,
                params=params
                )