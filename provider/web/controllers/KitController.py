from flask import redirect, flash
from provider.web.controllers.Controller import Controller

from octapus import OctapusCLI

class KitController(Controller):
    def __init__(self, request):
        super().__init__(request)

    def install(self):
        kitName = self.request.form['kit']

        OctapusCLI(args=['install:kit', kitName]).manager()

        flash(f'Kit {kitName} instalado com sucesso!', 'success')
        return redirect('/kits')
