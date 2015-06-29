
# Setup Javascript
from flask.ext.assets import Bundle, Environment

bundles = {
  'main.js': Bundle(
    'js/lib/d3.js',
    'js/draggable.js',
    'js/talk_graph.js',
    output='gen/main.js',
  ),
}

def register_javascripts(app):
  assets = Environment(app)
  assets.register(bundles)
