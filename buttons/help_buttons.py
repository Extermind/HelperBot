import discord
from discord.ui import Button


class PrevButton(Button):
    def __init__(self, ctx, label, currentPage, totalPages):
        super().__init__(label=label, style=discord.ButtonStyle.green)

        self.ctx = ctx
        self.currentPage = currentPage
        self.totalPages = totalPages
        self.check_if_disabled()

    def check_if_disabled(self):
        if self.currentPage <= 1:
            self.disabled = True
        else:
            self.disabled = False

    async def callback(self, interaction):
        await interaction.response.edit_message()
        page = int(self.currentPage)-1
        await self.ctx.invoke(self.ctx.bot.get_command('help'),page=page)

class NextButton(Button):
    def __init__(self, ctx, label, currentPage, totalPages):
        super().__init__(label=label, style=discord.ButtonStyle.green)

        self.ctx = ctx
        self.currentPage = currentPage
        self.totalPages = totalPages
        self.check_if_disabled()

    def check_if_disabled(self):
        if self.currentPage >= self.totalPages:
            self.disabled = True
        else:
            self.disabled = False

    async def callback(self, interaction):
        await interaction.response.edit_message()
        page = int(self.currentPage) + 1
        await self.ctx.invoke(self.ctx.bot.get_command('help'), page=page)

class PageButton(Button):
    def __init__(self, ctx,currentPage, totalPages):
        super().__init__(label=f'{currentPage}/{totalPages}', style=discord.ButtonStyle.gray)
        self.disabled = True
