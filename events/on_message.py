import nextcord
from nextcord.ext import commands
from tools.unit_conversion import replace_with_metric


class OnMessageEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return

        msg = replace_with_metric(message.content)
        if msg == message.content:
            return

        await message.channel.send("```" + msg + "```")


def setup(bot: commands.Bot):
    bot.add_cog(OnMessageEvent(bot))
