from flask import render_template, redirect, url_for
from provider.cli.web.controllers.Controller import Controller
from provider.cli.web.services.DecoratorServices import DecoratorServices
import os

from database.models.decorators import DecoratorsModel

class DecoratorController(Controller):
    def __init__(self, request):
        super().__init__(request)
        
    def store(self):
        command = self.request.form['command']
        decorator = self.request.form['decorator'][:-3]
        
        decoratorCode = f"{decorator}.{decorator.capitalize()}()"
        decoratorFile = f"application/decorators/{decorator}.py"
        commandFile = f"application/cogs/{command}.py"
        
        if not DecoratorsModel().filter(decoratorFile=decoratorFile, commandFile=commandFile).first():
            DecoratorServices(command, decoratorCode).run()
            DecoratorsModel().add(decoratorFile=decoratorFile, commandFile=commandFile)
        
        return redirect(self.request.referrer)
    
    def remove(self):
        id = self.request.form['id']
        
        DecoratorsModel().delete(id=id)
        
        return redirect(self.request.referrer)