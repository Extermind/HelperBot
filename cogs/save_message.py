import json
import os
from datetime import datetime

import discord
from discord.ext import commands
from discord import Button
from discord.ui import Button, View

import utils.utils
from Embeds.saved_messages_embed import SavedMessagesEmbed
from views import help_view


class SaveMessage(commands.Cog, name='Save Message Module'):
    def __init__(self, bot):
        self.bot = bot
        self.pageNumber = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name="save_message", aliases=["save_msg", "smsg"], description='Saves replied message')
    async def save_message(self, ctx):
        reference = ctx.message.reference
        if reference is None:
            return await ctx.reply("You did not reply to any message")

        # await reference.resolved.reply("Noticed",mention_author=False)

        fetch_message = await ctx.fetch_message(reference.message_id)
        # need to check if this message is a photo or a film
        if (len(fetch_message.attachments) > 0):
            att = {}
            i = 0
            for a in fetch_message.attachments:
                att.update({i: a.url})
                i+=1


        timestamp = datetime.timestamp(datetime.now())
        jsonObj = {
            "serverID": ctx.guild.id,
            "serverName": ctx.guild.name,
            "channelID": ctx.message.channel.id,
            "channelName": ctx.message.channel.name,
            "messageID": reference.message_id,
            "message": fetch_message.content,
            "creationTimeStamp": timestamp,
        }
        # print(jsonObj)
        embed = SavedMessagesEmbed(jsonObj)
        # print(embed)
        # print(ctx.author)
        await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(SaveMessage(bot))
