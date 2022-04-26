import os
from dotenv import load_dotenv

import utils.utils
from utils import *
from clients.bot_client import *
from cogs.err_handler import *
from cogs.greetings import *
from cogs.dynamic_channels import *


def main():
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    prefix = "."
    intents = discord.Intents.all()

    bot = BotClient(command_prefix=prefix, intents=intents,help_command=None)


    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    bot.run(token)

if __name__ == '__main__':
    main()