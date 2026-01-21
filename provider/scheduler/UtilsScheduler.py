from database.models.scheduler import SchedulerModel

class UtilsScheduler:
    def open(self, giveawayId, date):

        SchedulerModel().add(
            date=date,
            schedule='giveaways',
            scheduleId=giveawayId
        )

    def close(self, id):
        SchedulerModel().edit(where={'scheduleId':id}, activated=1)