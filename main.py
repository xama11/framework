from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from dotenv import load_dotenv
from provider.loaders.ComponentLoader import ComponentLoader
from provider.loaders.SchedulerLoader import SchedulerLoader
import discord
import os

load_dotenv()
                
class Bot(commands.Bot):
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=os.getenv('PREFIX'), intents=discord.Intents.all(), help_command=None)

    async def setup_hook(self):
        self.scheduler.start()
        
        await ComponentLoader(self).load()
        await SchedulerLoader(self.scheduler, self).load()
        
        for file in os.listdir("application/cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"application.cogs.{file[:-3]}")

bot = Bot()
bot.run(os.getenv('DISCORD_TOKEN'))