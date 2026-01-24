from provider.colors import *

class InfoFlag:
    def message(self):
        return f"""
{GREEN}Octapus CLI{RESET}

{GREEN}Usage:{RESET}
    {BLUE}python3 octapus.py command:area argument_name

{GREEN}Examples:{RESET}
    {BLUE}python3 octapus.py make:model User
    python3 octapus.py load:migration
{RESET}"""