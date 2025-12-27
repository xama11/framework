from discord import app_commands

def Hasadmin():
    async def wrap(interaction):
        if not interaction.user.guild_permissions.administrator: # Edit here
            raise HasadminError()
        return True
    return app_commands.check(wrap)

class HasadminError(app_commands.errors.CheckFailure):
    def __init__(self):
        super().__init__(f":x: message")
