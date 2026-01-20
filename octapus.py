import sys
import importlib
from typing import List, Optional

from database.models.terminals import TerminalsModel

from provider.cli.managers.FlagsManager import FlagsManager
from provider.cli.managers.CommandsManager import CommandsManager

from dotenv import load_dotenv
load_dotenv()

class OctapusCLI:
    
    def __init__(self, args = sys.argv[1:]):
        self.args = args
        
    def manager(self):
        return CommandsManager(self.args).manager() if not FlagsManager(self.args).run() else None

def main():
    try:
        result = OctapusCLI().manager()
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