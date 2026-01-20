from provider.colors import *

class HelpFlag:
    def message(self):
        return print(f"""
{GREEN}Octapus CLI

{GREEN}Usage:{RESET}
    python3 octapus.py command:area argument_name

{GREEN}Commands:{RESET}
    make:
        {BLUE}python3 octapus.py make:command argument_name
        python3 octapus.py make:container argument_name
        python3 octapus.py make:components argument_name
        python3 octapus.py make:decorator argument_name
        python3 octapus.py make:migration argument_name
        python3 octapus.py make:model argument_name
        python3 octapus.py make:scheduler argument_name{RESET}
    load:
        {BLUE}python3 octapus.py load:migrate{RESET}
""")