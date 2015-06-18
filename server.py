
# Main imports
from flask import Flask
app = Flask(__name__, static_url_path='/static')

# Setup SCSS
from flaskext.sass import sass
sass(app, input_dir='static/scss', output_dir='static/css')

# Rendering imports
from flask import render_template
from flask import send_from_directory
from flask import jsonify

from talk_db import all_talks
from compute_distances import distances

max_nodes = 10

# TODO : move into appropriate file
def edges(talks):
  d = distances(talks)
  num_nodes = max_nodes if max_nodes else len(d)

  e = []
  for i in xrange(num_nodes):
    for j in xrange(i + 1, num_nodes):
      e.append({ 'from': i, 'to': j, 'weight': d[i][j]})
      e.append({ 'from': j, 'to': i, 'weight': d[i][j]})
  return e

talks = all_talks()
if max_nodes:
  talks = talks[:max_nodes]
e = edges(talks)

@app.route('/')
def main():
  return render_template('main.html',
      num_talks=str(len(talks)),
      talks=talks,
      num_edges=str(len(e)),
      edges=e)

if __name__ == "__main__":
  app.run()
