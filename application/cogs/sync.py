from discord.ext import commands

# Do not remove this command if you want to use the slash commands.

class Sync(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx):
        if not ctx.author.guild_permissions.administrator: return
        await ctx.send("Carregando os comandos\n-# Isso pode demorar...")
        await self.bot.tree.sync()

async def setup(bot):
    await bot.add_cog(Sync(bot))
    