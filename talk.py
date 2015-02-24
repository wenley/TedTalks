
from bs4 import BeautifulSoup
import urllib2

def raw_html_for_url(url):
  return urllib2.urlopen(url).read()

def cached_value(method):
  cache_key = '_%s' % (method.__name__,)
  def wrap(self, *args, **kwargs):
    if hasattr(self, cache_key):
      return getattr(self, cache_key)
    setattr(self, cache_key, method(self, *args, **kwargs))
    return getattr(self, cache_key)
  wrap.__name__ = method.__name__
  return wrap

class Talk(object):
  def __init__(self, url, speaker=None, title=None, transcript=None):
    self.url = url
    self.language_url = url + '?language=en'
    self.transcript_url = url + '/transcript?language=en'

    if speaker:
      self._speaker = speaker
    if title:
      self._title = title
    if transcript:
      self._transcript = transcript

  def __repr__(self):
    return "<Talk '%s' by %s>" % (self.title(), self.speaker())

  @cached_value
  def speaker(self):
    return self.transcript_doc().find('meta', attrs={'name': 'author'})['content'].strip()

  @cached_value
  def title(self):
    return self.transcript_doc().find('h4', class_='h9 m5').find('a', href=self.language_url).string.strip()

  @cached_value
  def transcript_doc(self):
    return BeautifulSoup(raw_html_for_url(self.transcript_url))

  @cached_value
  def transcript(self):
    transcript_html = self.transcript_doc().find('div', class_='talk-transcript__body')
    text = ' '.join(tag.text for tag in transcript_html.find_all('span', class_='talk-transcript__fragment'))
    return text
