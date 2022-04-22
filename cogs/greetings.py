import discord
from discord.ext import commands
from discord.ui import Button, View

from asyncio import TimeoutError

class Greetings(commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hi", help="says hi to you <3",aliases=["hello","hewwo"])
    async def greeting(self, ctx):
        await ctx.channel.send(f"Hewwo {ctx.message.author.name}!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Wewcome tuwu ouw sewvew {member.mention}')

    @commands.command(name="hlep")
    async def helpComm(self, ctx):
        button1 = Button(label="“Click me!", style=discord.ButtonStyle.green)

        button3 = Button(label="Danger", style=discord.ButtonStyle.danger)

        view = View()
        view.add_item(button1)

        view.add_item(button3)

        await ctx.send("Hi!", view=view)