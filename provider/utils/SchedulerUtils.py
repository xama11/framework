from database.models.scheduler import Scheduler

class SchedulerUtils:
    def open(giveawayId, date):

        Scheduler().add(
            date=date,
            schedule='giveaways',
            scheduleId=giveawayId
        )

    def close(self, id):
        Scheduler().edit(where={'scheduleId':id}, activated=1)