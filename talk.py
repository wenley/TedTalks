
from bs4 import BeautifulSoup
import urllib2

def raw_html_for_url(url):
  return urllib2.urlopen(url).read()

class Talk(object):
  def __init__(self, url):
    self.url = url
    self.language_url = url + '?language=en'
    self.transcript_url = url + '/transcript?language=en'

  def speaker(self):
    return self.transcript_doc().find('meta', attrs={'name': 'author'})['content'].strip()

  def title(self):
    return self.transcript_doc().find('h4', class_='h9 m5').find('a', href=self.language_url).string.strip()

  def transcript_doc(self):
    if hasattr(self, '_transcript_doc'):
      return self._transcript_doc
    self._transcript_doc = BeautifulSoup(raw_html_for_url(self.transcript_url))
    return self._transcript_doc

  def transcript(self):
    transcript_html = self.transcript_doc().find('div', class_='talk-transcript__body')
    text = ' '.join(tag.text for tag in transcript_html.find_all('span', class_='talk-transcript__fragment'))
    return text
