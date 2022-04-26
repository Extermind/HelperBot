from datetime import datetime
import json
import os

import discord
from discord.ext import commands
from discord.utils import get

class DynamicChannels(commands.Cog, name="Dynamic Channels Module"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded.')

    @commands.command(name="create_dynamic_channels", aliases=["create_channels"], description='Creates new dynamic channel group and role for you and your friend')
    async def create_dynamic_channel_group(self, ctx, group_name):
        guild = ctx.guild
        path = f"guilds/{guild.id}/{ctx.author.id}"
        timestamp = datetime.timestamp(datetime.now())
        # create role if not exists
        if os.path.isfile(path + "/dynamicChannelData.json"):
            await ctx.channel.send("You already have dynamic channel QnQ")
            return
        name = ctx.author.name + "'s " + group_name
        role = await guild.create_role(name=name)
        # assing roles to channel owner
        await ctx.author.add_roles(role)
        # create overwrite
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }
        # create category
        category = await guild.create_category(group_name)
        await category.edit(overwrites=overwrites)
        # create channels
        text_channel = await guild.create_text_channel(f"{group_name}-text", category=category)
        await text_channel.edit(sync_permissions=True)
        voice_channel = await guild.create_voice_channel(f"{group_name}-vc", category=category)
        await  voice_channel.edit(sync_permissions=True)
        # create simple data base for the active dynamic channel
        jsonObj = {
            "userID": ctx.author.id,
            "roleID": role.id,
            "categoryID": category.id,
            "categoryName": name,
            "creationTimeStamp": timestamp,
        }
        # create dir for a member if do not exist
        path = f"guilds/{guild.id}/{ctx.author.id}"
        if not os.path.isdir(path):
            os.mkdir(path)
        # create that file and dump json data
        path = path + "/dynamicChannelData.json"
        f = open(path, 'w')
        json.dump(jsonObj, f)
        f.close()

    @commands.command(name="delete_dynamic_channels", description='Deletes your dynamic channel')
    async def delete_dynamic_channel_group(self, ctx):
        guild = ctx.guild
        path = f"guilds/{guild.id}/{ctx.author.id}/dynamicChannelData.json"
        if os.path.isfile(path):
            f = open(path)
            jsonObj = json.load(f)
            f.close()
            os.remove(path)
            category = get(guild.categories,id=jsonObj['categoryID'])
            if category is not None:
                for channel in category.channels:
                    await channel.delete()
            await category.delete()
            role = get(guild.roles, id=jsonObj['roleID'])
            if role is not None:
                for user in role.members:
                    await user.remove_roles(role)
            await role.delete()

    @commands.command(name="add_friend_to_channel_group", description='Adds your friends to your group by username')
    async def add_friend_to_channel_group(self, ctx, friend_name):
        guild = ctx.guild
        path = f"guilds/{guild.id}/{ctx.author.id}/dynamicChannelData.json"
        if os.path.isfile(path):
            f = open(path)
            jsonObj = json.load(f)
            f.close()
        else:
            await  ctx.channel.send("You do not own any kind of dynamic channel group")
            return
        if jsonObj['userID'] != ctx.author.id:
            await ctx.channel.send("You are not an owner o this channels group...")
            return
        # check if author have a role thats exatly the same as his id
        roleID = jsonObj['roleID']
        role = get(ctx.guild.roles,id=roleID)
        # if yes search for his friend and add this role
        friend = get(ctx.guild.members, name=friend_name)
        if friend is None:
            await ctx.channel.send("There is no such member QuQ")
            return
        if friend is ctx.author:
            await  ctx.channel.send("You can't add yourself to group that you own")
            return

        await friend.add_roles(role)
        await ctx.channel.send(f"user: `{friend.name}` was added to the group")

    @commands.command(name="remove_friend_from_channel_group", description="Removes your friend from group by name")
    async def remove_friend_from_channel_group(self, ctx, friend_name):
        guild = ctx.guild
        path = f"guilds/{guild.id}/{ctx.author.id}/dynamicChannelData.json"
        if os.path.isfile(path):
            f = open(path)
            jsonObj = json.load(f)
            f.close()
        else:
            await  ctx.channel.send("You do not own any kind of dynamic channel group")
            return
        if jsonObj['userID'] != ctx.author.id:
            await ctx.channel.send("You are not an owner o this channels group...")
            return
        #check if this friend has role of the channel group
        friend = get(ctx.guild.members, name=friend_name)
        if friend is None:
            await ctx.channel.send("There is no such member QuQ")
            return
        if friend is ctx.author:
            await ctx.channel.send("You can't remove yourself from the group that you own")
            return
        #get role id and role
        roleID = jsonObj['roleID']
        role = get(ctx.guild.roles, id=roleID)
        if role in friend.roles:
            await friend.remove_roles(role)
            await ctx.channel.send(f"user: `{friend.name}` was removed from group")


def setup(bot):
    bot.add_cog(DynamicChannels(bot))
