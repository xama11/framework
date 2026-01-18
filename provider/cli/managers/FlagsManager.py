class FlagsManager:
    def __init__(self, args):
        self.args = args

    def run(self):
        flags = self._parse()

        if not flags: return False

        for flag in flags:
            print(flag)

        return True
        

    def _parse(self):
        return [flag for flag in self.args if '--' in flag]