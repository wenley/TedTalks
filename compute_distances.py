
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

def distances(talks):
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

if __name__ == "__main__":
  talks = all_talks()

  d = distances(talks)

  for i in xrange(len(d)):
    for j in xrange(len(d[i])):
      if i == j:
        continue
      print -1 / math.log(d[i][j]), talks[i], talks[j]

