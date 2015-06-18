
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
from compute_distances import scores, similarities

max_nodes = None

# TODO : move into appropriate file
import numpy
def edges(talks):
  edge_scores = scores(similarities(talks))
  raw_scores = [score for inner in edge_scores.itervalues() for score in inner.itervalues()]
  top_20_percent_cutoff = numpy.percentile(raw_scores, 95)

  normalize = lambda score: score / top_20_percent_cutoff

  num_nodes = max_nodes if max_nodes else len(edge_scores)

  e = []
  for i in xrange(num_nodes):
    for j in xrange(i + 1, num_nodes):
      if edge_scores[i][j] < top_20_percent_cutoff:
        continue
      e.append({ 'from': i, 'to': j, 'weight': normalize(edge_scores[i][j])})
      e.append({ 'from': j, 'to': i, 'weight': normalize(edge_scores[i][j])})
  return e

talks = all_talks()
if max_nodes:
  talks = talks[:max_nodes]
e = edges(talks)

@app.route('/')
def main():
  return render_template('main.html')

@app.route('/static/js/<path:path>')
def send_js(path):
  return send_from_directory('static/js', path)

@app.route('/edges.json')
def edges():
  nodes = [{ 'title': talk.title() } for talk in talks]
  links = [{
    'source': edge['from'],
    'target': edge['to'],
    'value': edge['weight'],
    } for edge in e]
  return jsonify(nodes=nodes, links=links)

if __name__ == "__main__":
  app.run()
