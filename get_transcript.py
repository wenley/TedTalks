
from bs4 import BeautifulSoup
from talk import Talk

if __name__ == '__main__':
  with open('test_data/lessig.html') as f:
    lessig_doc = BeautifulSoup(f.read())

  lessig = Talk('http://www.ted.com/talks/lawrence_lessig_the_unstoppable_walk_to_political_reform')
  lessig._transcript_doc = lessig_doc

  # print lessig.transcript()
  print lessig.speaker()
  print lessig.title()
