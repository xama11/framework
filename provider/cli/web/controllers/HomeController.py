from flask import render_template, redirect, url_for
from provider.cli.web.controllers.Controller import Controller
import os

from database.models.migrations import MigrationsModel
from database.models.terminals import TerminalsModel

class HomeController(Controller):
    def __init__(self, request):
        super().__init__(request)
    
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