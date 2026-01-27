from flask import request
from provider.octapus.web.controllers.DecoratorController import DecoratorController

def router(app):
    @app.route("/decorator/add", methods=['POST'])
    def decoratorsAdd():
        return DecoratorController(request).store()

    @app.route("/decorator/remove", methods=['POST'])
    def decoratorsRemove():
        return DecoratorController(request).remove()
