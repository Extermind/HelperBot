import discord
from discord.ext import commands
from discord.ui import Button, View

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



    # @commands.command(name="hlep")
    # async def helpComm(self, ctx):
    #     button1 = Button(label="“Click me!", style=discord.ButtonStyle.green)
    #
    #     button3 = Button(label="Danger", style=discord.ButtonStyle.danger)
    #
    #     async def button_callback(interaction):
    #         await interaction.response.send_message("Henloo QwQ")
    #
    #     button1.callback = button_callback
    #
    #
    #
    #     view = View()
    #     view.add_item(button1)
    #     view.add_item(button3)
    #     await ctx.send(view=view)

def setup(bot):
    bot.add_cog(Greetings(bot))

