from discord.ext import commands
from discord import app_commands
from application.decorators._enum import *

# Your imports

from application.containers.example import ExampleContainer # python3 octapus.py make:container Example
from application.containers.components.example import * # python3 octapus.py make:components Example

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.container = ExampleContainer()

    @app_commands.command(name="example", description="Example description")
    @cooldown.cooldown('example', seconds=100)
    async def example(self, interaction):
        ...
        
    # the example for @example is the name of the command function
    @example.error
    async def error(self, interaction, error):
        if interaction.response.is_done():
            await interaction.response.send_message(error, ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(Example(bot))
