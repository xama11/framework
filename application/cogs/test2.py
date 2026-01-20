from discord.ext import commands
from discord import app_commands
from application.decorators._enum import *

# Your imports

from application.containers.test2 import Test2Container # python3 octapus.py make:container Test2
from application.containers.components.test2 import * # python3 octapus.py make:components Test2

class Test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.container = Test2Container()

    @app_commands.command(name="test2", description="Test2 description")
    @cooldown.cooldown('test2', seconds=100)
    async def test2(self, interaction):
        ...
        
    # the test2 for @test2 is the name of the command function
    @test2.error
    async def error(self, interaction, error):
        if interaction.response.is_done():
            await interaction.response.send_message(error, ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(Test2(bot))
