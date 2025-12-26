import sys
import importlib
from typing import List, Optional
from pathlib import Path

from database.models.terminals import TerminalsModel

from dotenv import load_dotenv
load_dotenv()

class OctapusCLI:
    PROVIDER_PATH = 'provider/cli'
    
    def __init__(self, args= sys.argv[1:]):
        self.args = args
        self.cmd = self.args[0] if self.args else None
        self.parts = self.cmd.split(':')
        self.name = None
        
    def manager(self):
        if self.args[0] == '--help': return self.show_help()
        
        if not self.args or not self.cmd or ':' not in self.cmd:
            return self.show_info()
        
        try:
            command, area = self._parse_command()
        except ValueError as e:
            return f"Error: {e}"
        
        if not self._command_exists(command):
            return f"Error: Command '{command}' does not exist"
        
        if len(self.args) < 2:
            if (self.parts[0]=='load'):
                return self.run_command(command, area)
            return self.show_info()
        
        self.name = self.args[1]
        
        try:
            return self.run_command(command, area)
        except Exception as e:
            return f"Error executing command: {e}"
    
    def _parse_command(self):
        if len(self.parts) != 2:
            
            raise ValueError("Command format must be 'command:area'")
        
        command, area = self.parts
        
        if not command or not area:
            raise ValueError("Command and area cannot be empty")
        
        return command, area
    
    def _command_exists(self, command: str):
        command_path = Path(self.PROVIDER_PATH) / f'{command}.py'
        return command_path.exists()
    
    def show_help(self):
        return """
Octapus CLI Tool
================

Usage:
    python3 octapus.py command:area argument_name

Commands:
    make:
        python3 octapus.py make:command argument_name
        python3 octapus.py make:container argument_name
        python3 octapus.py make:components argument_name
        python3 octapus.py make:decorator argument_name
        python3 octapus.py make:migration argument_name
        python3 octapus.py make:model argument_name
        python3 octapus.py make:scheduler argument_name
    load:
        python3 octapus.py load:migrate
"""
    
    def show_info(self):
        info = """
Octapus CLI Tool
================

Usage:
    python3 octapus.py command:area argument_name

Examples:
    python3 octapus.py make:model User
    python3 octapus.py load:migration

Format:
    - command: The action to perform
    - area: The target area/context
    - argument_name: The name/identifier for the operation

Available commands are located in: provider/cli/
        """
        return info.strip()
    
    def run_command(self, command: str, area: str):
        try:
            module_path = f'provider.cli.{command}'
            module = importlib.import_module(module_path)
            
            class_name = command.capitalize()
            command_class = getattr(module, class_name)
            
            instance = command_class(command, area, self.name)
            
            result = instance.run()
            TerminalsModel().add(command=f'{command}:{area} {self.name}')
            return result
            
        except ImportError as e:
            raise ImportError(f"Failed to import command module '{command}': {e}")
        except AttributeError as e:
            raise AttributeError(
                f"Command class '{command.capitalize()}' not found in module: {e}"
            )

def main():
    try:
        cli_tool = OctapusCLI()
        result = cli_tool.manager()
        print(result) if result else None
        return 0
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        return 130
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())