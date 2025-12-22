from flask import render_template

import os

from database.models.migrations import MigrationsModel
from database.models.terminals import TerminalsModel

class HomeController():
    def __init__(self, request):
        self.request = request
    
    def view(self):
        commands = len([file for file in os.listdir('application/cogs/') if file.endswith('.py')])
        
        migrations = [migration for migration in MigrationsModel().get().limit(10).all() if not migration[1][0]=='0']
        terminals = TerminalsModel().get().limit(10).orderBy('id').all()

        return render_template(
            'home.html',
            commands=commands,
            migrations=migrations,
            terminals=terminals
        )