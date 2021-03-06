import discord
import sys
import traceback
from discord.ext import commands

class ErrHandler(commands.Cog, name='Error Handling Module'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            await ctx.channel.send(f'I can\'t find `{ctx.message.content}` command QnQ')
        else:
            print('Ignoring Exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)




def setup(bot):
    bot.add_cog(ErrHandler(bot))
