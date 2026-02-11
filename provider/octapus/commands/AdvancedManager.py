from database.models.terminals import TerminalsModel
from provider.octapus.messages.help import HelpMessage
from provider.octapus.messages.info import InfoMessage
from pathlib import Path
import os
import importlib

class AdvancedManager:
    def __init__(self, args):
        self.args = args
        self.providerPath = 'provider/octapus'
        self.cmd = self.args[0] if self.args else None

    def validator(self):
        if not self.args or not self.cmd or ':' not in self.cmd:
            return InfoMessage().message()
        
        self.parts = self.cmd.split(':')

        try:
            command, area = self._parse_command()
        except ValueError as e:
            return f"Error: {e}"
        
        if not self._command_exists(command):
            return f"Error: Command '{command}' does not exist"
        
        if len(self.args) < 2: return InfoMessage().message()
        
        try:
            return self._run_command(command, area)
        except Exception as e:
            return f"Error executing command: {e}"

    def _run_command(self, command: str, area: str):
        try:
            module = importlib.import_module(f'provider.octapus.commands.advanceds.{command}')
            
            commandClass = getattr(module, command.capitalize())
            
            instance = commandClass(command, area, self.args[1])
            
            result = instance.run()
            TerminalsModel().add(command=f'{command}:{area} {self.args[1]}')
            return result
            
        except ImportError as e:
            raise ImportError(f"Failed to import command module '{command}': {e}")
        except AttributeError as e:
            raise AttributeError(
                f"Command class '{command.capitalize()}' not found in module: {e}"
            )

    def _parse_command(self):
        
        if len(self.parts) != 2:
            raise ValueError("Command format must be 'command:area'")
        
        command, area = self.parts
        
        if not command or not area:
            raise ValueError("Command and area cannot be empty")
        
        return command, area

    def _command_exists(self, command: str):
        commandPath = Path(self.providerPath)/f'commands/advanceds/{command}.py'
        return commandPath.exists()