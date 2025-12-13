from datetime import datetime, timedelta
from provider.bases.BaseScheduler import BaseScheduler
from database.models.scheduler import Scheduler
from provider.utils.SchedulerUtils import *

# Your imports

class Example(BaseScheduler):
    def __init__(self, scheduler, bot):
        super().__init__(
            scheduler=scheduler,
            table="example",  # Name of the database table
            name="example"    
        )
        self.bot = bot

    # id = ExampleId
    async def register(self, id, seconds):  # Create a new scheduled task
        date = datetime.now()+timedelta(seconds=seconds) # NOT DELETE
        SchedulerUtils.open(id, date) # NOT DELETE
        
        self.scheduler.add_job(self.run, 'date', run_date=date, args=[id])

    
    async def run(self, id):
        SchedulerUtils.close(self, id) # NOT DELETE
        
        date = self.getAction(id)
        print(date)
