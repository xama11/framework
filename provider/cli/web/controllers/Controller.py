import os

class Controller:
    def __init__(self, request):
        self.request = request
        self.decorators = []
        
        self.setValues()
        
        
    def setValues(self):
        self.decorators = [decorator for decorator in os.listdir('application/decorators') if decorator.endswith('.py')]
        