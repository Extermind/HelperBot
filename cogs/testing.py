import re

import discord
from discord.ext import commands
from discord import Button
from discord.ui import Button, View
from views import help_view


class Testing(commands.Cog, name='Testing Module'):
    def __init__(self, bot):
        self.bot = bot
        self.pageNumber = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name="test")
    async def test(self, ctx, str):
        embed = discord.Embed(description="l",url=str)
        await ctx.channel.send(embed=embed)
        pass



def setup(bot):
    bot.add_cog(Testing(bot))
