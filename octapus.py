import sys
import os
import importlib
from typing import List, Optional

from provider.colors import RED, RESET

from database.models.terminals import TerminalsModel

from provider.octapus.managers.CommandsManager import CommandsManager

from dotenv import load_dotenv
load_dotenv()

class OctapusCLI:
    def __init__(self, args = sys.argv[1:]):
        self.args = args
        
    def manager(self):
        return CommandsManager(self.args).manager()

def main():
    try:
        if not (os.path.exists('.env')):
            print(f'\n{RED} [ERROR] Your project not have .env!\n{RESET}')
            exit()

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