from nextcord.ext import commands

class ReadyCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"We have logged in as {self.bot.user}")

def setup(bot: commands.Bot):
    bot.add_cog(ReadyCog(bot))
