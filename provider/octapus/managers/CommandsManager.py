from database.models.terminals import TerminalsModel
from provider.octapus.messages.help import HelpMessage
from provider.octapus.messages.info import InfoMessage
from pathlib import Path
import os
import importlib

from provider.octapus.commands.BasicManager import BasicManager
from provider.octapus.commands.AdvancedManager import AdvancedManager

class CommandsManager:
    def __init__(self, args):
        self.args = args
        self.providerPath = 'provider/octapus'
        self.cmd = self.args[0] if self.args else None

    def manager(self):
        type = self._identify_type()

        validator =  BasicManager(self.args).validator() if (type == 'basic') else AdvancedManager(self.args).validator()
        return validator

    def _identify_type(self): # Types: Basic and Advanced
        if (len(self.args)==1) and not ':' in self.args[0]:
            return 'basic'
        else:
            return 'advanced'