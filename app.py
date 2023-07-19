from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello!'

@app.route('/howareyou')
def how_are_you():
    return 'How are you?'

if __name__ == '__main__':
    # Use Gunicorn as the WSGI server
    from gunicorn.app.base import BaseApplication
    class FlaskApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:8080',
        'workers': 4
    }

    FlaskApplication(app, options).run()
