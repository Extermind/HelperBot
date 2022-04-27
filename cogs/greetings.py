import asyncio

import discord
from discord.ext import commands


class Greetings(commands.Cog, name='Greetings Module'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name="hi", description="says hi to you <3",aliases=["hello","hewwo"])
    async def greeting(self, ctx):
        await ctx.channel.send(f"Hewwo {ctx.message.author.name}!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Wewcome tuwu ouw sewvew {member.mention}')







def setup(bot):
    bot.add_cog(Greetings(bot))

