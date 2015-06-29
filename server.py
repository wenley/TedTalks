
# Main imports
from flask import Flask
app = Flask(__name__, static_url_path='/static')

# Setup SCSS
from flaskext.sass import sass
sass(app, input_dir='static/scss', output_dir='static/css')

# Set routes
from setup.router import register_routes
register_routes(app)

# # Setup Javascript
# from setup.javascripts import register_bundles
# register_bundles(app)

if __name__ == "__main__":
  app.run()
