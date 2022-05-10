import discord


class SavedMessagesEmbed(discord.Embed):
    def __init__(self, data, color):
        super().__init__(title=f"Saved Message from **{data['serverName']}**", color=color)
        self.add_field(name="Channel: ", value=data['channelName'], inline=False)
        self.add_field(name="Message: ", value=data['message'], inline=False)
        if len(data['attachments']) > 0:
            str = ''
            for key, val in data['attachments'].items():
                str += val + '\n'
            self.add_field(name="Attachments: ", value=str)
        if len(data['films']) > 0:
            str = ''
            for key, val in data['films'].items():
                str += val + '\n'
            self.add_field(name="Films: ", value=str)

class SavedMessagesImageEmbed(discord.Embed):
    def __init__(self, img_url, color):
        super().__init__(color=color)
        self.set_image(url=img_url)
