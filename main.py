import os
from dotenv import load_dotenv
from clients.bot_client import *
from cogs.err_handler import *
from cogs.greetings import *
from cogs.dynamic_channels import *


def main():
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    prefix = "."
    intents = discord.Intents.all()

    bot = BotClient(command_prefix=prefix, intents=intents)

    # Error handler class
    bot.add_cog(ErrHandler(bot))
    # Greetings class
    bot.add_cog(Greetings(bot))
    # dynamic channels
    bot.add_cog(DynamicChannels(bot))

    bot.run(token)

if __name__ == '__main__':
    main()