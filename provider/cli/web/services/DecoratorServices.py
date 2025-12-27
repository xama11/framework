import ast

class AddDecorator(ast.NodeTransformer):
    def __init__(self, command, decoratorName):
        self.command = command
        self.decoratorName = decoratorName
    
    def visit_AsyncFunctionDef(self, node):
        if node.name == self.command:
            decorator = ast.Name(id=self.decoratorName, ctx=ast.Load())
            node.decorator_list.insert(3, decorator)
        return node

class DecoratorServices:
    def __init__(self, command, decoratorName):
        self.command = command
        self.decoratorName = decoratorName

    def addDecorator(self, source_code: str) -> str:
        tree = ast.parse(source_code)
        
        tree = AddDecorator(self.command, self.decoratorName).visit(tree)
        
        ast.fix_missing_locations(tree)
        return ast.unparse(tree)

    def run(self):

        with open(f"application/cogs/{self.command}.py", "r") as f:
            code = f.read()

        newCode = self.addDecorator(code)

        with open(f"application/cogs/{self.command}.py", 'w') as code:
            code.write(newCode)