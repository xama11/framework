from flask import render_template, redirect, url_for
from provider.web.controllers.Controller import Controller
import os

from database.models.migrations import MigrationsModel
from database.models.terminals import TerminalsModel

class HomeController(Controller):
    def __init__(self, request):
        super().__init__(request)
    
    def view(self):
        migrations = [file for file in sorted(os.listdir('database/migrations/')) if file.endswith('.py') and not '0' in file[0]]
        terminals = TerminalsModel().get().limit(10).orderBy('id').all()

        return render_template(
            'home.html',
            commands=self.commands,
            migrations=migrations,
            terminals=terminals
        )