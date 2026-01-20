from provider.cli.messages.help import HelpFlag

class FlagsManager:
    def __init__(self, args):
        self.args = args

    def results(self):
        return {
            'help': HelpFlag().message
            }
    
    # Return True: stop and run only flag
    # Return False: no run flag, run command
    def run(self):
        flags = self._parse()

        if not flags: return False

        for flag in flags:
            name = flag[2:]

            if not name in self.results():
                raise Exception(f' [ERROR] Invalid flag: --{name}')
            
            self.results()[name]()
        return True

    def _parse(self):
        return [flag for flag in self.args if '--' in flag]