from flask import Flask
import importlib
import os

#############
#
# -> Dashboard Web
# Open your terminald and use: `python3 web.py` to open.abs
#
#############

app = Flask(__name__,
            template_folder='provider/octapus/web/templates')

for file in os.listdir('provider/octapus/web/routes/'):
    if file.endswith('.py') and not '0' in file[0]:
        print(f'Loading {file} routes')
        module = importlib.import_module(f'provider.octapus.web.routes.{file[:-3]}')
        router = module.router(app)

if __name__ == '__main__':
    app.run(debug=True)