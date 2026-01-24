import os

class Controller:
    def __init__(self, request):
        self.request = request
        self.decorators = []
        self.commands = []
        
        self.setValues()
        
        
    def setValues(self):
        self.decorators = [decorator for decorator in os.listdir('application/decorators') if decorator.endswith('.py') and not '_' in decorator]
        self.commands = [file for file in os.listdir('application/cogs/') if file.endswith('.py')]