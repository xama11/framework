from provider.migrations.LoadMigrations import LoadMigrations
from provider.colors import *

from provider.octapus.messages.help import HelpMessage

class Help:
    def __init__(self, command):
        self.command = command
        
    def run(self):
        return HelpMessage().message()