import discord


class SavedMessagesEmbed(discord.Embed):
    def __init__(self, data):
        super().__init__(title=f"Saved Message from **{data['serverName']}**", color=0xFFA500)
        super().add_field(name="Channel: ", value=data['channelName'], inline=False)
        super().add_field(name="Message: ", value=data['message'],inline=False)
