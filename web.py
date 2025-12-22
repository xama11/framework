from flask import Flask, request, render_template

from provider.cli.web.controllers.HomeController import HomeController
from provider.cli.web.controllers.MigrationsController import MigrationsController

app = Flask(__name__,
            template_folder='provider/cli/web/templates')

@app.route("/")
def home():
    return HomeController(request).view()

@app.route("/credits")
def credits():
    return render_template('credits.html')

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

if __name__ == '__main__':
    app.run(debug=True)