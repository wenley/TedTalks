
# Rendering imports
from flask import render_template
from flask import send_from_directory
from flask import jsonify

from talk_db import all_talks
from compute_distances import scores, similarities

max_nodes = 10

# TODO : move into appropriate file
import numpy
def edges(talks):
  edge_scores = scores(similarities(talks))
  raw_scores = [score for inner in edge_scores.itervalues() for score in inner.itervalues()]
  top_20_percent_cutoff = numpy.percentile(raw_scores, 80)
  normalize = lambda score: score / top_20_percent_cutoff

  num_nodes = max_nodes if max_nodes else len(edge_scores)

  e = []
  for i in xrange(num_nodes):
    for j in xrange(i + 1, num_nodes):
      e.append({ 'from': i, 'to': j, 'weight': normalize(edge_scores[i][j])})
      e.append({ 'from': j, 'to': i, 'weight': normalize(edge_scores[i][j])})

  return e

talks = all_talks()
if max_nodes:
  talks = talks[:max_nodes]
e = edges(talks)

def main():
  return render_template('main.html')

def send_js(path):
  return send_from_directory('static/js', path)

def edges():
  nodes = [{ 'title': talk.title() } for talk in talks]
  links = [{
    'source': edge['from'],
    'target': edge['to'],
    'value': edge['weight'],
    } for edge in e]
  return jsonify(nodes=nodes, links=links)

####################################

routes = {
  '/': main,
  '/static/js/<path:path>': send_js,
  '/edges.json': edges
}

def register_routes(app):
  for path, route in routes.iteritems():
    app.route(path)(route)
