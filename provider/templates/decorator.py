from discord import app_commands

def Example():
    async def wrap(interaction):
        if not interaction.user.guild_permissions.administrator: # Edit here
            raise ExampleError()
        return True
    return app_commands.check(wrap)

class ExampleError(app_commands.errors.CheckFailure):
    def __init__(self):
        super().__init__(f":x: message")
