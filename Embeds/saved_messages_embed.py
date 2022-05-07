import discord


class SavedMessagesEmbed(discord.Embed):
    def __init__(self, data):
        super().__init__(title=f"Saved Message from **{data['serverName']}**", color=0xFFA500)
        self.add_field(name="Channel: ", value=data['channelName'], inline=False)
        self.add_field(name="Message: ", value=data['message'], inline=False)
        if len(data['attachments']) > 0:
            str = ''
            for key, val in data['attachments'].items():
                str += val + '\n'
            self.add_field(name="Attachments: ", value=str)

class SavedMessagesImageEmbed(discord.Embed):
    def __init__(self, img_url):
        super().__init__(color=0xFF69B4)
        self.set_image(url=img_url)
