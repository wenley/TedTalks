
# Main imports
from flask import Flask
app = Flask(__name__, static_url_path='/static')

# Setup SCSS
from flaskext.sass import sass
sass(app, input_dir='static/scss', output_dir='static/css')

# Configuration steps
import setup
setup.router.register_routes(app)
setup.javascripts.register_javascripts(app)

if __name__ == "__main__":
  app.run()
