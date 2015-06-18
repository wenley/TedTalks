
import math
import numpy
import lda
from talk_db import all_talks
from collections import defaultdict

import scipy.sparse

def word_matrix(talks):
  def word_count(talk):
    def add_word(d, word):
      d[word] += 1
      return d
    return reduce(add_word, talk.transcript().split(), defaultdict(lambda: 0))
  word_counts = map(word_count, talks)

  words = reduce(lambda words, counts: words | set(counts.iterkeys()), word_counts, set())
  word_to_index = { word: index for (index, word) in enumerate(words) }

  shape = (len(talks), len(words))
  X = numpy.ndarray(shape)

  for i, counts in enumerate(word_counts):
    for word, count in counts.iteritems():
      j = word_to_index[word]
      X[i][j] = count
  return X

def model_for_matrix(X):
  model = lda.LDA(n_topics=20, n_iter=100, random_state=19)
  return model.fit(X)

def cosine_similarity(a, b):
  return numpy.dot(a, b) / (numpy.linalg.norm(a) * numpy.linalg.norm(b))

# Range of values: (0, 1)
# 1 = identical
# 0 = no relation
def similarities(talks):
  X = word_matrix(talks)
  model = model_for_matrix(X)

  doc_topics = model.doc_topic_
  min_val = doc_topics.max()
  normalized = doc_topics / min_val

  d = defaultdict(lambda: {})
  for i in xrange(len(normalized)):
    for j in xrange(i + 1, len(normalized)):
      distance = cosine_similarity(normalized[i], normalized[j])
      d[i][j] = distance
      d[j][i] = distance
  return d

# Range of values: (1, Infinity)
# Infinity = Identical
# 1 = no relation
def score(similarity):
  return -1 /math.log(similarity)

def scores(d):
  score = lambda similarity: -1 / math.log(similarity)

  return {
      i: {
        j: score(sim) for j, sim in inner.iteritems()
        } for i, inner in d.iteritems()
      }

# Range of values: (1, Infinity)
# 1 = identical
# Infinity = no relation
def distances(d):
  raw_scores = [score(value) for inner in d.itervalues() for value in inner.itervalues()]
  cutoff_score = numpy.percentile(raw_scores, 80)

  distance = lambda score: 1 + (cutoff_score / score)
  squared = lambda x: x * x

  return {
      i: {
        j: squared(distance(score(similarity)))
        for j, similarity in inner.iteritems()
        } for i, inner in d.iteritems()
      }

def print_stats(raw):
  print "Mean:", numpy.mean(raw)
  print "StdD:", numpy.std(raw)
  print "80th:", numpy.percentile(raw, 80)
  print "90th:", numpy.percentile(raw, 90)
  print "95th:", numpy.percentile(raw, 95)
  print numpy.histogram(raw, 30)

if __name__ == "__main__":
  talks = all_talks()

  d = similarities(talks)
  dists = distances(d)
  num_talks = len(talks)
  num_to_display = 10

  # for i in xrange(0, num_talks, num_talks / num_to_display):
  #   for j in xrange(0, num_talks, num_talks / num_to_display):
  #     if i == j:
  #       continue
  #     similarity = d[i][j]
  #     distance = dists[i][j]
  #     print similarity, score(similarity), distance

  raw_sims = [s for inner in d.itervalues() for s in inner.itervalues()]
  raw_scores = [score(s) for s in raw_sims]
  raw_distances = [dist for inner in dists.itervalues() for dist in inner.itervalues()]

  print "Similarities:"
  print_stats(raw_sims)

  print "\n\nScores:"
  print_stats(raw_scores)
  
  print "\n\nDistances:"
  print_stats(raw_distances)
