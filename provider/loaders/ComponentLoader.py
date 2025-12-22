import os
import importlib
import ast

class ComponentLoader:
    def __init__(self, bot):
        self.bot = bot
    
    async def load(self):
        basePath = 'application/containers'

        for file in os.listdir(basePath):
            if not file.endswith(".py"): continue

            name = file.replace('.py', '')

            containerFile = importlib.import_module(f'application.containers.{name}')
            containerClass = getattr(containerFile, f'{name.capitalize()}Container')
            
            with open(basePath+f'/components/{name}.py', 'r') as file:
                componentCode = file.read()
                
            tree = ast.parse(componentCode)
            classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
            
            for className in classes:
                if 'Modal' in className: continue
                if 'TMP' in className[0]: continue
                
                componentFile = importlib.import_module(f'application.containers.components.{name}')
                componentClass = getattr(componentFile, f'{className}')
                
                self.bot.add_view(componentClass(containerClass()))