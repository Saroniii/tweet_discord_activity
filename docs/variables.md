### What is written in this docs?

Variables that can be used where sentences of an activity tweet.

## OK, How to use variables on activity tweet sentence?

You can apply it to the template on lines 11-13 of configs/twitter.py.

## What variables are available?

This is the list of variables that can be used.

| Variable name       | Variable description                                                                                    | Example of returning a value          | 
| ------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------- | 
| owner               | Return activity bot owner.                                                                              | example#1234                          | 
| owner_name          | Return activity bot owner name.                                                                         | example                               | 
| owner_discriminator | Return activity bot owner discriminator.                                                                | 1234                                  | 
| owner_id            | Return activity bot owner id.                                                                           | 123456789123456789                    | 
| status              | Return activity bot owner status.<br>(The display language depends on the configuration profile.)       | English:online<br>Japanese:オンライン | 
| activity            | Return activity bot owner activity.<br>(If the activity could not be obtained, None will be displayed.) | Minecraft                             | 
| time                | Returns the current time.<br>(Depends on the hosting server time setting.)                              | 12:34                                 | 
| time_month_and_day  | Returns the current month and day.<br>(Depends on the server's time setting.)                           | 2/11                                  | 
| time_year           | Returns the current year.<br>(Depends on the hosting server time setting.)                              | 2020                                  | 
| time_month          | Returns the current month.<br>(Depends on the hosting server time setting.)                             | 2                                     | 
| time_day            | Returns the current day.<br>(Depends on the server's time setting.)                                     | 11                                    | 
| time_hour           | Returns the current hour.<br>(Depends on the hosting server time setting.)                              | 12                                    | 
| time_minute         | Returns the current minute.<br>(Depends on the hosting server time setting.)                            | 34                                    | 
| time_second         | Returns the current second.<br>(Depends on the hosting server time setting.)                            | 30                                    | 

## Hmm. Please provide a specific example of how to fill out the form.

| Example sentence              | Example return sentence      | 
| ----------------------------- | ---------------------------- | 
| I started playing (activity)! | I started playing Minecraft! | 
| I'm (status) now!             | I'm online now!              | 

## How can I add custom variables?

Add the variable you want to add and its return value in the variable section of the link below.
The method of addition should be based on the Python dict type.

https://github.com/Saroniii/tweet_discord_activity/blob/main/utils/tweet.py#L38