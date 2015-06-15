
# Main imports
from flask import Flask
app = Flask(__name__)

# Rendering imports
from flask import render_template

from talk_db import all_talks
from compute_distances import distances

# TODO : move into appropriate file
def edges(talks):
  d = distances(talks)

  e = []
  for i in xrange(len(d)):
    for j in xrange(i + 1, len(d)):
      e.append({ 'from': i, 'to': j, 'weight': d[i][j]})
      e.append({ 'from': j, 'to': i, 'weight': d[i][j]})
  return e

talks = all_talks()
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
