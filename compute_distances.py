
import lda
from talk_db import all_talks
from collections import defaultdict

def word_matrix():
  talks = all_talks()

  def word_count(talk):
    def add_word(d, word):
      d[word] += 1
      return d
    return reduce(add_word, talk.transcript().split(), defaultdict(lambda: 0))
  word_counts = map(word_count, talks)

  words = reduce(lambda words, counts: words | set(counts.iterkeys()), word_counts, set())
  word_to_index = { word: index for (index, word) in enumerate(words) }

  print len(words)

if __name__ == "__main__":
  word_matrix()
