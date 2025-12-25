from flask import render_template, redirect, url_for
from provider.cli.web.controllers.Controller import Controller
from octapus import OctapusCLI
import os

from database.models.decorators import DecoratorsModel

class CommandController(Controller):
    def __init__(self, request):
        super().__init__(request)
    
    def view(self):
        
        commands = [file for file in os.listdir('application/cogs/') if file.endswith('.py')]
        
        return render_template(
            'commands.html',
            commands=commands
        )
        
    def edit(self, name):
        with open(f'application/cogs/{name}.py') as file:
            file = file.read()
            
        yourDecorators = DecoratorsModel().filter(commandFile=f'application/cogs/{name}.py').all()
        
        print(yourDecorators)
        
        return render_template('commands-edit.html',
            name=name,
            file=file,
            decorators=self.decorators,
            yourDecorators=yourDecorators
        )
        
    def update(self, name):
        form = self.request.form
        
        with open(f'application/cogs/{name}.py', 'w') as file:
            file.write(form['code'])
        
        return redirect(self.request.referrer)
    
    def store(self):
        name = str(self.request.form['name'])

        OctapusCLI(args=['make:command', name]).manager() 
        OctapusCLI(args=['make:container', name]).manager() 
        OctapusCLI(args=['make:components', name]).manager() 
            
        return redirect(self.request.referrer)