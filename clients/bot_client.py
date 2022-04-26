import discord
from discord.ext import commands
from utils.utils import create_dir_if_not_exist

class BotClient(commands.Bot):
    async def on_ready(self):
        print(f'{self.user.name} has connected do Discord!\n\nLoading Cogs: ')

        #check for folder where data is stored
        create_dir_if_not_exist('guilds')

    async def on_guild_join(self, guild):
        # create data base for this server
        create_dir_if_not_exist(f'guilds/{guild.id}')

        general = guild.text_channels[0]
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title="**======== *Thanks For Adding Me!* ========**", description=f"""
                   Thanks for adding me to {guild.name}!
                   You can use the `.help` command to get started!
                   """, color=0xd89522)
            await general.send(embed=embed)

