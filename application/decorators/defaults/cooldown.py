from discord import app_commands
from datetime import datetime, timezone

from database.models.cooldowns import Cooldowns

def Cooldown(cmd, seconds):
    async def wrap(interaction):
        cool = Cooldowns().filter(userId=interaction.user.id, command=cmd).first()
        
        if (cool):
            coolDate = datetime.strptime(cool[3], "%Y-%m-%d %H:%M:%S.%f")
            nowDate = datetime.now()
            
            diff = int((nowDate - coolDate).total_seconds())

            if (diff > seconds):
                Cooldowns().edit(where={'userId':interaction.user.id, 'command':cmd}, lastUsed=str(nowDate))
                return True
            
            raise CooldownError(diff, seconds)
        
        Cooldowns().add(userId=interaction.user.id, command=cmd, lastUsed=datetime.now())
        return True
    return app_commands.check(wrap)

class CooldownError(app_commands.errors.CheckFailure):
    def __init__(self, cooldownSeconds, seconds):
        super().__init__(f":x: You cannot use this command right now, please wait {seconds-cooldownSeconds} seconds to use it again.")
