import os
import importlib
import ast

class ComponentRegister:
    def __init__(self, bot):
        self.bot = bot
    
    async def load(self):
        basePath = 'application/containers'

        for file in os.listdir(basePath):
            if not file.endswith(".py"): continue

            name = file.replace('.py', '')

            with open(f'{basePath}/{file}', 'r', encoding='utf-8') as source_file:
                containerCode = source_file.read()

            containerTree = ast.parse(containerCode)
            className = None
            for node in ast.walk(containerTree):
                if isinstance(node, ast.ClassDef) and node.name == name:
                    className = node.name
                    break
            
            if className is None:
                continue

            containerFile = importlib.import_module(f'application.containers.{name}')
            containerClass = getattr(containerFile, className)
            
            with open(basePath+f'/components/{name}.py', 'r', encoding='utf-8') as file:
                componentCode = file.read()
                
            tree = ast.parse(componentCode)
            classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
            
            for className in classes:
                if 'Modal' in className: continue
                if 'TMP' in className[:3]: continue
                
                componentFile = importlib.import_module(f'application.containers.components.{name}')
                componentClass = getattr(componentFile, f'{className}')
                
                self.bot.add_view(componentClass(containerClass()))
