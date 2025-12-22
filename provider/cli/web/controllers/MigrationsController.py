from flask import render_template, redirect, url_for

import os

from octapus import OctapusCLI

from database.models.migrations import MigrationsModel
from database.models.terminals import TerminalsModel

class MigrationsController():
    def __init__(self, request):
        self.request = request
    
    def view(self):
        migrations = [file for file in sorted(os.listdir('database/migrations/')) if file.endswith('.py') and not '0' in file[0]]
        
        migrations_status = []
        
        for file in migrations:
            infos = MigrationsModel().filter(migration=file[:-3]).first()
            
            migrations_status.append({
                    'name':infos[1] if infos else file[:-3],
                    'activated': infos[2] if infos else None
                })
        
        return render_template(
            'migrations.html',
            migrations=migrations_status
        )
        
    def edit(self, name):
    
        with open(f'database/migrations/{name}.py') as file:
            file = file.read()
        
        return render_template('migrations-edit.html',
            name=name,
            file=file
            )
        
    def update(self, name):
        form = self.request.form
        
        with open(f'database/migrations/{name}.py', 'w') as file:
            file.write(form['code'])
        
        return redirect(self.request.referrer)

    def store(self):
        name = str(self.request.form['name'])

        OctapusCLI(args=['make:migration', name]).manager() 
            
        return redirect(self.request.referrer)