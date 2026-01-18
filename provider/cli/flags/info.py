class InfoFlag:
    def message():
        return """
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