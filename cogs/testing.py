import discord
from discord.ext import commands
from discord import Button
from discord.ui import Button, View


class Testing(commands.Cog, name='Testing Module'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    class MyView(View):
        def __init__(self, ctx):
            super().__init__()
            self.ctx = ctx


        @discord.ui.button(label='click me', style=discord.ButtonStyle.green)
        async def button_callback(self,button,interaction):
            # red text won't apear
            await interaction.response.edit_message()
            await self.ctx.send("it works")


    @commands.command(name="hlep")
    async def helpComm(self, ctx):
        view = self.MyView(ctx)
        await ctx.send(view=view)


def setup(bot):
    bot.add_cog(Testing(bot))