### What is written in this docs?

The specific use of this bot.

## What do I need to do first to use it?

You have to meet three minimum requirements to be able to use this Bot.

1) Create a Bot to monitor activities and invite it on ONLY ONE SERVER.

2) You, the owner of the Bot, MUST BE A MEMBER OF THE SERVER INDICATED IN 1.

3) You have the necessary information for the correct activation.

## OK, What do I need first?

There are two things you must get:

1) Four items including your own Twitter access token (API Key, API secret, Access token, Token secret)

How to get: https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/

2) Tokens for Activity Bot

How to get: https://www.writebots.com/discord-bot-token/

## I got it! What to do next?

Describe the data, as in twitter_template.py:

In Line 5~8, describe the tokens you get on Twitter, etc., looking at the comments.

## Okay, Can I use this?

There is one more step! This is the last!

Set the Bot token.

There are two ways to do this.
The first is to set the token in the environment variable "TOKEN" (recommended)

This is recommended if you want to launch it on Heroku or something similar!

Second, set a token in configs/token.py (deprecated)

This is recommended if you do not want to add environment variables.

However, it is not recommended unless you want to use it in an environment where there is a risk of token leakage and where security can be guaranteed.

## Okay, How do I start?

If you use Windows...
> Click startup.bat

If not...
> Use command line and open main.py

## I got it up! I want to change the message in my activity tweet, how do I do it?

Check out [variable docs](https://github.com/Saroniii/tweet_discord_activity/blob/main/docs/variables.md)
