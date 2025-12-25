from flask import Flask, request, render_template

from provider.cli.web.controllers.HomeController import HomeController
from provider.cli.web.controllers.MigrationsController import MigrationsController
from provider.cli.web.controllers.CommandController import CommandController
from provider.cli.web.controllers.DecoratorController import DecoratorController

app = Flask(__name__,
            template_folder='provider/cli/web/templates')

@app.route("/")
def home():
    return HomeController(request).view()

@app.route("/credits")
def credits():
    return render_template('credits.html')

## CommandController
@app.route("/commands")
def commands():
    return CommandController(request).view()

@app.route("/command/<name>")
def commandEdit(name):
    return CommandController(request).edit(name)

@app.route("/command/<name>", methods=['POST'])
def commandUpdate(name):
    return CommandController(request).update(name)

@app.route("/command/create", methods=['POST'])
def commandCreate():
    return CommandController(request).store()

## CommandController
@app.route("/migrations")
def migrations():
    return MigrationsController(request).view()

@app.route("/migration/<name>")
def migrationsEdit(name):
    return MigrationsController(request).edit(name)

@app.route("/migration/<name>", methods=['POST'])
def migrationsUpdate(name):
    return MigrationsController(request).update(name)

@app.route("/migration/create", methods=['POST'])
def migrationsCreate():
    return MigrationsController(request).store()

## Decorators
@app.route("/decorator/add", methods=['POST'])
def decoratorsAdd():
    return DecoratorController(request).store()

@app.route("/decorator/remove", methods=['POST'])
def decoratorsRemove():
    return DecoratorController(request).remove()

if __name__ == '__main__':
    app.run(debug=True)