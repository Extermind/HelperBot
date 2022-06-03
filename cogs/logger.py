from discord.ext import commands


class Logger(commands.Cog, name="Logger Module"):
    def __init__(self, bot):
        self.bot = bot
        self.log = False

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name="logger", aliases=['log'], description='turn on or of log')
    async def logger(self, ctx):
        self.log = True




def setup(bot):
    bot.add_cog(Logger(bot))