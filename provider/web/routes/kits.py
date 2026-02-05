from flask import request, render_template
from provider.web.controllers.KitController import KitController

def router(app):
    @app.route("/kits")
    def kits():
        return render_template('kits.html')
        
    @app.route("/kits/install", methods=["POST"])
    def install():
        return KitController(request).install()
