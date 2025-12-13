from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self, ):
        print()
        print(f" BOT INICIADO -> {self.bot.user} (ID: {self.bot.user.id})")
        print()

async def setup(bot):
    await bot.add_cog(Events(bot))

