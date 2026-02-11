from database.models.terminals import TerminalsModel
from provider.octapus.messages.help import HelpMessage
from provider.octapus.messages.info import InfoMessage
from pathlib import Path
import os
import importlib

class BasicManager:
    def __init__(self, args):
        self.args = args
        self.providerPath = 'provider/octapus'
        self.cmd = self.args[0] if self.args else None

    def validator(self):
        if not self._command_exists(self.cmd):
            return f"Error: Command '{self.cmd}' does not exist"
        
        try:
            return self._run_command()
        except Exception as e:
            return f"Error executing command: {e}"
        
    def _run_command(self):
        try:
            module = importlib.import_module(f'provider.octapus.commands.basics.{self.cmd}')
            commandClass = getattr(module, self.cmd.capitalize())
            instance = commandClass(self.cmd)
            
            result = instance.run()
            return result
            
        except ImportError as e:
            raise ImportError(f"Failed to import command module '{self.cmd}': {e}")
        except AttributeError as e:
            raise AttributeError(
                f"Command class '{self.cmd.capitalize()}' not found in module: {e}"
            )

    def _command_exists(self, command: str):
        commandPath = Path(self.providerPath)/f'commands/basics/{command}.py'
        return commandPath.exists()