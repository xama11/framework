from flask import Flask
import importlib
import os

from provider.colors import *

# -> Dashboard Web
# Open your terminald and use: `python3 web.py` to open.

if not (os.path.exists('.env')):
    print(f'\n{RED} [ERROR] Your project not have .env!\n{RESET}')
    exit()

app = Flask(__name__,
            template_folder='provider/web/templates')
app.secret_key = os.getenv('SECRET_KEY', 'xama11_sk_web')

for file in os.listdir('provider/web/routes/'):
    if file.endswith('.py'):
        module = importlib.import_module(f'provider.web.routes.{file[:-3]}')
        router = module.router(app)

if __name__ == '__main__':
    app.run(debug=True)