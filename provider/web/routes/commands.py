from flask import request
from provider.web.controllers.CommandController import CommandController

def router(app):
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
