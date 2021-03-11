# TwitterBot
Code relating to my twitter bot, which can be found [here](https://twitter.com/WhatDoITweetBot). (The bot and the template are both WIP.)

## Setup
### API Tokens
Get your [Twitter api tokens](https://developer.twitter.com/en/support/twitter-api).
### Config File
Create a copy of `configs/template.ini` as `configs/config.ini` and store your credentials in it.

## Development
To create commands for your bot:
1. Create a `Command` subclass using the `Command` Abstract Base Class.
2. Import the command into `client.py`
3. Add the command to the `commands_dict` in `client.py` along with an alias for twitter users.