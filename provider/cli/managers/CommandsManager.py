from provider.cli.flags.help import HelpFlag
from provider.cli.flags.info import InfoFlag

from database.models.terminals import TerminalsModel

import importlib

from pathlib import Path
import os

class CommandsManager:
    def __init__(self, args):
        self.args = args
        self.provider_path = 'provider/cli'
        self.cmd = self.args[0] if self.args else None
        self.parts = self.cmd.split(':')

    def manager(self):
       
        if not self.args or not self.cmd or ':' not in self.cmd:
            return InfoFlag.message()
        
        try:
            command, area = self._parse_command()
        except ValueError as e:
            return f"Error: {e}"
        
        if not os.path.exists(f'provider/cli/{command}.py'):
            return f"Error: Command '{command}' does not exist"
        
        if len(self.args) < 2: return InfoFlag.message()
        
        try:
            return self.run_command(command, area)
        except Exception as e:
            return f"Error executing command: {e}"

    def run_command(self, command: str, area: str):
        try:
            module = importlib.import_module(f'provider.cli.{command}')
            
            className = command.capitalize()
            commandClass = getattr(module, className)
            
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
        command_path = Path(self.provider_path) / f'{command}.py'
        return command_path.exists()