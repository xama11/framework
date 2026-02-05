from flask import request, render_template
from provider.web.controllers.HomeController import HomeController

def router(app):
    @app.route("/")
    def home():
        return HomeController(request).view()

    @app.route("/credits")
    def credits():
        return render_template('credits.html')
