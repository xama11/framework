from flask import render_template, redirect, url_for
from provider.cli.web.controllers.Controller import Controller
import os

from database.models.decorators import DecoratorsModel

class DecoratorController(Controller):
    def __init__(self, request):
        super().__init__(request)
        
    def store(self):
        decorator = self.request.form['decorator']
        command = self.request.form['command']
        
        decoratorFile = f'application/decorators/{decorator}'
        commandFile = f'application/cogs/{command}.py'
        
        if not DecoratorsModel().filter(decoratorFile=decoratorFile, commandFile=commandFile).first():
            DecoratorsModel().add(decoratorFile=decoratorFile, commandFile=commandFile)
        
        with open (f'application/cogs/{command}.py') as file:
            file = file.read()
            
        with open('application/cogs/eee.py', 'w') as code:
            code.write(file)
        
        # return redirect(self.request.referrer)
        return file
    
    def remove(self):
        id = self.request.form['id']
        
        DecoratorsModel().delete(id=id)
        
        return redirect(self.request.referrer)