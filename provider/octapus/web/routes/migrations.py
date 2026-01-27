from flask import request
from provider.octapus.web.controllers.MigrationsController import MigrationsController

def router(app):
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
