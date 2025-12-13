import click
from dotenv import load_dotenv
from provider.bases.BaseLoader import BaseLoader 

load_dotenv()

@click.command()
@click.option("--container", help="Create a container")
@click.option("--decorator", help="Create a decorator")
@click.option("--scheduler", help="Create a scheduler")
@click.option("--migration", help="Create a migration")
@click.option("--model", help="Create a model")
@click.option("--load", help="Load your database")
@click.option("--ccc", help="Create a container, components e command")
def officialCLI(container, decorator, scheduler, migration, model, ccc, load):
    """by: silvaleal"""

    if load:
        if str(load).lower() == 'migrate':
            loader = BaseLoader()
            loader.run()
    else:
        if container:
            _build_('container', container)
            _build_('components', container)
        elif decorator:
            _build_('decorator', decorator)
        elif scheduler:
            _build_('scheduler', scheduler)
        elif migration:
            _build_('migration', migration)
        elif model:
            _build_('model', model)
        elif ccc:
            _build_('command', ccc)
            _build_('container', ccc)
            _build_('components', ccc)
        else:
            print('\ndpy2-framework by silvaleal\n -> Use `python cli.py --help`')

def _paths_(area):
    arr = {
        "command": 'application/cogs',
        "container": 'application/containers',
        "components": "application/containers/components",
        "decorator": "application/decorators",
        "migration": "database/migrations",
        "model": "database/models",
        "scheduler": "application/schedulers",
    }
    return arr[area]

def _build_(area, name):
    with open(f'provider/templates/{area}.py', 'r') as original:
        original = original.read().replace('Example', str(name)).replace('example', str(name).lower())
    
    with open(f'{_paths_(area)}/{str(name).lower()}.py', 'w') as file:
        file.write(original)

if __name__ == '__main__':
    officialCLI()