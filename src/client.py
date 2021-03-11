"""
Run me!
(from root directory)
conda activate twitterbot
python src\client.py --config configs\config.ini
"""
import argparse
import configparser

from triggers import MentionsListener
from interactions import CommandManager, MentionsLogger
import commands

import twitter

commands_dict = {
    #'topics': commands.LDA,
}

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='configuration file')


if __name__ == '__main__':
    #load configs
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    keys = config['Twitter Keys']

    api = twitter.Api(
        consumer_key=keys['API_Key'],
        consumer_secret=keys['API_Secret_Key'],
        access_token_key=keys['Access_Token'],
        access_token_secret=keys['Access_Token_Secret'],
        tweet_mode="extended",
    )

    paths = config['Paths']

    command_manager = CommandManager(api, commands_dict, commands.Help)
    mentions_listener = MentionsListener(api, paths['Latest_Mentions_ID'])
    mentions_logger = MentionsLogger(paths['Mentions_Log'])

    print(dict(keys))
    print(dict(paths))
    #print(api.GetFriends())

    for mention in mentions_listener.listen(verbose=True):
        mentions_logger.log(mention)
        cmd = command_manager.parse(mention)
        output = cmd.reply_tweet()


