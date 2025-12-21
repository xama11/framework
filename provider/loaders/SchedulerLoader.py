import os
import importlib

class SchedulerLoader:
    def __init__(self, scheduler, bot):
        self.scheduler = scheduler
        self.bot = bot
        
    async def load(self):
        for file in os.listdir('application/schedulers'):
            if file.endswith('.py'):
                name = file.replace('.py', '')
                module = importlib.import_module(f'application.schedulers.{name}')
                moduleClass = getattr(module, f'{name.capitalize()}Scheduler')
                moduleClass = moduleClass(self.scheduler, self.bot)
                
                for schedulerEnable in moduleClass.getSchedulers():
                    print(schedulerEnable)
                    moduleClass.saveSchedule(moduleClass.run, schedulerEnable)