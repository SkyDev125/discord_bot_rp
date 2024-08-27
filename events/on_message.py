import nextcord
from nextcord.ext import commands


class OnMessageEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return
        await message.channel.send(message.content)


def setup(bot: commands.Bot):
    bot.add_cog(OnMessageEvent(bot))
