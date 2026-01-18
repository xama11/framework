class HelpFlag:
    def message():
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