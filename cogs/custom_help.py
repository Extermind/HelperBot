import math
import random

import discord
from discord import Colour
from discord.ext import commands
from discord.ui import Button, View


class CustomHelp(commands.Cog, name="Custom Help Module"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name='help', aliases=['h', 'commands'], description='Help command!')
    async def help_com(self, ctx, page=1):
        helpEmbed = discord.Embed(
            title='================== List of commands! ==================', color=Colour.random()
        )
        # helpEmbed.set_thumbnail(url=ctx.me.avatar_url)

        cogs = [c for c in self.bot.cogs.keys()]
        # I do not have Events class yet soo
        #cogs.remove('events')
        # but I Do have err handling module that has 0 commands, so I have to remove it
        cogs.remove('Error Handling Module')
        cogs.remove('Testing Module')

        cogsPerPage = 2
        totalPages = math.ceil(len(cogs) / cogsPerPage)

        page = int(page)
        if page > totalPages or page < 1:
            await ctx.send(f'Invalid page numebr: {page}')
            return
        helpEmbed.set_footer(
            text=f'{page}/{totalPages} Pages'
        )

        neededCogs = []
        for i in range(cogsPerPage):
            x = i + (int(page) - 1) * cogsPerPage
            try:
                neededCogs.append(cogs[x])
            except IndexError:
                pass

        for cog in neededCogs:
            commandList = ""
            for command in self.bot.get_cog(cog).walk_commands():
                if command.hidden:
                    continue
                elif command.parent != None:
                    continue
                commandList += f'**{command.name}** - *{command.description}*\n'
            commandList += "\n"

            helpEmbed.add_field(name=cog, value=commandList, inline=False)

        await ctx.channel.send(embed=helpEmbed)


def setup(bot):
    bot.add_cog(CustomHelp(bot))
