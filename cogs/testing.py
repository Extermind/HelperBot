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


    @commands.command(name="hlep")
    async def helpComm(self, ctx,number=1):
        self.pageNumber=number
        view = help_view.HelpView(ctx,self)
        await ctx.send(view=view)


def setup(bot):
    bot.add_cog(Testing(bot))