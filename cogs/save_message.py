import json
import os
from datetime import datetime

import discord
from discord.ext import commands
from discord import Button
from discord.ui import Button, View

import utils.utils
from views import help_view

class SaveMessage(commands.Cog, name='Save Message Module'):
    def __init__(self, bot):
        self.bot = bot
        self.pageNumber = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')


    @commands.command(name="save_message", aliases=["save_msg","smsg"], description='Saves replied message')
    async def save_message(self, ctx):
        reference = ctx.message.reference
        if reference is None:
            return await ctx.reply("You did not reply to any message")
        path = f"guilds/{ctx.guild.id}/{ctx.message.author.id}"
        utils.utils.create_dir_if_not_exist(path)

        await reference.resolved.reply("Noticed",mention_author=False)

        reference_id = reference.cached_message.id
        reference_content = reference.cached_message.content

        timestamp = datetime.timestamp(datetime.now())
        jsonObj = {
            "serverID": ctx.guild.id,
            "serverName": ctx.guild.name,
            "channelID": ctx.message.channel.id,
            "channelName": ctx.message.channel.name,
            "messageID": reference_id,              # I tried to do it like reference.cached_message.id but it raise an error on None idk why
            "message": reference_content,           # same as above ant it's only because the channelID and channelName
            "creationTimeStamp": timestamp,
        }
        print(jsonObj)

# add show saved messages command
#   this command shows in private conversations with bot
#   all of that server/user saved messages and also have
#   a navigation buttons for example 5 messages per embed
#   or custom number per embed


def setup(bot):
    bot.add_cog(SaveMessage(bot))