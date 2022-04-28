import discord
from discord.ui import View,Button

from buttons.help_buttons import *


class HelpView(View):
    def __init__(self, ctx, currentPage=1, totalPages=1):
        super().__init__()
        self.ctx = ctx
        self.currentPage = currentPage
        self.totalPages = totalPages
        self.prevbtn = PrevButton(self.ctx,"<",self.currentPage,self.totalPages)
        self.pagebtn = PageButton(self.ctx,self.currentPage,self.totalPages)
        self.nextbtn = NextButton(self.ctx,">",self.currentPage,self.totalPages)
        self.add_item(self.prevbtn)
        self.add_item(self.pagebtn)
        self.add_item(self.nextbtn)

    # async def prev_btn_callback(self,interaction,ctx):
    #     await interaction.response.edit_message()
    #     await self.ctx.send("Prev Button!")




    # @discord.ui.button(label='prevous Page', style=discord.ButtonStyle.green, disabled=True if self.currentPage==1else False )
    # async def button_callback(self, button, interaction):
    #     # red text won't apear
    #     await interaction.response.edit_message()
    #
    #     await self.ctx.send("it works")
    #     await self.ctx.send(int(self.parent.pageNumber) + 1)
    #
    # @discord.ui.button( )
