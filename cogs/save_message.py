import re
from datetime import datetime

import discord
from discord import Colour
from discord.ext import commands

import utils.utils as utils
from Embeds.saved_messages_embed import SavedMessagesEmbed, SavedMessagesImageEmbed


class SaveMessage(commands.Cog, name='Save Message Module'):
    def __init__(self, bot):
        self.bot = bot
        self.pageNumber = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name="save_message", aliases=["save_msg", "smsg"], description='Saves replied message')
    async def save_message(self, ctx):
        reference = ctx.message.reference
        if reference is None:
            return await ctx.reply("You did not reply to any message")

        fetch_message = await ctx.fetch_message(reference.message_id)
        color = Colour.random()
        data_from_message = self.message_links(fetch_message.content, color)
        # print("message:")
        # print(data_from_message)

        try:
            i_img = list(data_from_message[0])[-1]
            if i_img > 0:
                i_img += 1
        except IndexError:
            i_img = 0
        finally:
            try:
                i_film = list(data_from_message[1])[-1]
                if i_film > 0:
                    i_film += 1
            except IndexError:
                i_film = 0
            finally:
                data_from_attachments = self.attachments(fetch_message.attachments,color,i_img, i_film)
                # print("attachments:")
                # print(data_from_attachments)

                attachments = {}
                attachments.update(data_from_message[0])
                attachments.update(data_from_attachments[0])

                films = {}
                films.update(data_from_message[1])
                films.update(data_from_attachments[1])

                embeds = [*data_from_message[2], *data_from_attachments[2]]

                timestamp = datetime.timestamp(datetime.now())

                if fetch_message.content == '':
                    fmsg = "none"
                else:
                    fmsg = fetch_message.content

                jsonObj = {
                    "serverID": ctx.guild.id,
                    "serverName": ctx.guild.name,
                    "channelID": ctx.message.channel.id,
                    "channelName": ctx.message.channel.name,
                    "messageID": reference.message_id,
                    "message": fmsg,
                    "attachments": attachments,
                    "films": films,
                    "creationTimeStamp": timestamp,
                }
                # print(jsonObj)
                embeds.insert(0, SavedMessagesEmbed(jsonObj,color))
                try:
                    await self.send_embeds(embeds, ctx.author)
                except discord.errors.Forbidden:
                    await ctx.reply("Your DMs are turned off.\nRMC on server icon -> Privacy Settings -> Allow direct messages from server members.")



    # this works only for commandError not http need to try except :)
    # @save_message.error
    # async def save_message_error(self,ctx,error):
    #     if isinstance(error, discord.errors.Forbidden):
    #         await ctx.channel.send('Turn on your DMs b-baka QwQ')


    def message_links(self, message: str, color: int) -> tuple:
        # check if message content has jpg,png,gif and creates list of embed
        # returns tuple: dictionary of link, list of embeds
        img = {}
        film = {}
        att_embeds = []
        # checking if message have any links
        regex = r'(https?):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
        urls = re.findall(regex, message)
        if len(urls) > 0:
            i_img = 0
            i_film = 0
            for url_t in urls:
                url = f'{url_t[0]}://{url_t[1]}{url_t[2]}'
                temp = url.split('http')  # check for ex: "https://www.google.comhttps://www.bing.com" 
                temp.pop(0)
                for t in temp:
                    if utils.check_if_url_is_film(t):
                        film.update({i_film: f"http{t}"})
                        i_film += 1
                    elif utils.check_if_url_is_img(t):
                        img.update({i_img: f"http{t}"})
                        att_embeds.append(SavedMessagesImageEmbed(f"http{t}", color))
                        i_img += 1

        return (img, film, att_embeds)

    def attachments(self, att: list, color: int, i_img: int = 0, i_film: int = 0) -> tuple:
        # check if message has attachments and creates list of embed
        # returns tuple: dictionary of link, list of embeds
        img = {}
        film = {}
        att_embeds = []
        if len(att) > 0:
            for a in att:
                if utils.check_if_url_is_film(a.url):
                    film.update({i_film: a.url})
                    i_film += 1
                elif utils.check_if_url_is_img(a.url):
                    img.update({i_img: a.url})
                    att_embeds.append(SavedMessagesImageEmbed(a.url, color))
                    i_img += 1
        return (img, film, att_embeds)

    async def send_embeds(self, embeds_array, user: discord.Member):
        for e in embeds_array:
            await user.send(embed=e)
        pass


def setup(bot):
    bot.add_cog(SaveMessage(bot))
