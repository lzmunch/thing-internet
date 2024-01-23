import os
import traceback
import time
import re
import random
#
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
# from textblob import TextBlob
#
import constants

def get_base_url(full_url):
  """
  Get base url from input. Example:
    input - https://www.wikipedia.org/wiki/Sandwich
    returns - https://www.wikipedia.org
  """
  split_url = urlparse(full_url)
  return split_url.scheme + '://' + split_url.netloc

def rand_img_url(thing='fish'):
  """ Get url to "random" fake image """
  return random.choice(constants.LINK_DICT[thing])


def rand_word(thing='fish'):
  """ Get random phrase related to thing """
  return random.choice(constants.WORD_DICT[thing])

# def insert_things_nltk(thing, text):
#   if not text:
#     return text

#   blob = TextBlob(text)
#   nouns = [t for t in blob.tags if 'NN' in t[1]]
#   replace_count = max(1, text.count(' ') // 10)
#   if nouns:
#     word = nouns[0]
#     new_text = text.replace(word, rand_word(thing))
    
  return new_text

def insert_things(thing, text):
  """ Insert random words in random places """
  # TODO: make this work

    
  if not text:
    return text
  
  words = [w for w in text.split(' ') if w.isalpha()]
  n = len(words) // 20
  replace_words = random.sample(words, n)
  for rw in replace_words:
    text = text.replace(rw, rand_word(thing))
    # print('replacing {}'.format(rw))
  return text

def fix_domain(url_to_scrape, rel_link):
  """
  If link is relative, return link that has correct domain name prefixed
  
  Relative link identifiers:
    - starts with /
    - starts with ../
  
  Args:
  TODO
  """
  # print('fixing link:', rel_link)
  # starts with / but want to avoid catching // on accident
  check1 = rel_link[0] == '/' and rel_link[1] != '/'  
  check2 = rel_link[:3] == '../'

  # if not relative, do nothing
  if not (check1 or check2): 
    return rel_link

  base_url = get_base_url(url_to_scrape)
  
  # remove ../ if it is there
  if check2:
    rel_link = rel_link[2:]
    
  # base url might have / at end, e.g. "google.com/"  
  if base_url[-1] == '/':
    return base_url[:-1] + rel_link
  else:
    return base_url + rel_link
  
def get_soup(url_to_scrape):
  """
  Helper function to request data from url and soupify
  
  Args:
    url_to_scrape (str): e.g. https://www.wikipedia.org
    
  Returns:
    bs4.BeautifulSoup
  """
  try:
    html_text = requests.get(url_to_scrape).text
  except Exception as e:
    print(e)
    return None
  soup = BeautifulSoup(html_text, features="html.parser")
  return soup


def thingify(thing, url_to_scrape):
  """
  Process html_text from url_to_scrape
 
  Args:
    url_to_scrape (str): e.g. https://www.wikipedia.org
    
  Returns:
    str
  """
  # print(get_base_url(url_to_scrape))
  
  soup = get_soup(url_to_scrape)
  if not soup:
    return None

  # replace images
  scraped_img_tags = soup.findAll('img')
  img_css = 'max-width:500px;max-height:500px;'
  for i, img in enumerate(scraped_img_tags):
    img['src'] = rand_img_url(thing)
    img['srcset'] = rand_img_url(thing)
    if 'style' in img:
      img['style'] = img['style'] + ';' + img_css
    else:
      img['style'] = img_css
    
  # replace text
  paragraphs = soup.findAll('p')
  for p in paragraphs:
    # if p.text:
    #   p.string = insert_things(thing, p.text)
    # else:
    #   p.insert(0,rand_word(thing) + " ")
    # word_count = p.text.split(' ')
    # positions = random.sample(range(word_count), n)
    # p.insert(0,rand_word(thing) + " ")
#     spaces = [i.start() for i in re.finditer(' ', p.text.strip('  '))]
#     # print(spaces)
#     if spaces:
#       n = max(1, len(spaces) // 10)
#       for i in range(n):
#         idx = random.choice(spaces)
#         print(idx, p.text[idx:idx+10])
#         p.insert(idx, ' ' + rand_word(thing))
#     else:
#       p.insert(0,rand_word(thing) + " ")
      
    p.insert(0,rand_word(thing) + " ")
        
  
  tag_list = soup.findAll('strong')
  tag_list += soup.findAll('h1')
  tag_list += soup.findAll('h2')
  tag_list += soup.findAll('h3')
  for a in tag_list:
    if a.string:
      a_str = a.string.encode('utf-8')
      a.string = thingify_text(thing, a_str)

  # replace links
  tag_list = soup.findAll('a')
  
  # first replace link text
  for a in tag_list:
    if a.string:
      a_str = a.string.encode('utf-8')
      a.string = thingify_text(thing, a_str)

  # now try to replace link hrefs
  tag_list = soup.findAll('a', href=True)
  tag_list += soup.findAll('link', href=True)
  for tag in tag_list:
    # attempt to replace relative links to images
    # if any(ext in a['href'].lower() for ext in constants.EXT_LIST):
    #   a['href'] = rand_img()
    #   continue
    try:
      tag['href'] = fix_domain(url_to_scrape, tag['href'])
      # print('fixed link: {}'.format(tag['href']))
    except:
      pass 
  
  # TODO try to pull external .css and overwrite broken URLs?
  
  # try to fix relative links used by script tags
  script_tags = soup.findAll('script', src=True)
  for tag in script_tags:
    tag['src'] = fix_domain(url_to_scrape, tag['src'])
    # print('fixed script: {}'.format(tag['src']))

  # modify head - add jquery and client.js
  head = soup.find('head')
  if head:
    head.append(soup.new_tag("script", 
                              src="https://code.jquery.com/jquery-2.2.1.min.js",
                              integrity="sha256-gvQgAFzTH6trSrAWoH1iPo9Xc96QxSZ3feW6kem+O00=",
                              crossorigin="anonymous"))
    
    head.append(soup.new_tag("script", src="/public/client.js"))
    
    head.append(soup.new_tag("script", src="/public/iframeResizer.contentWindow.min.js"))
   
    # append 'thing' to title
    title = head.find('title')
    if title:
      title.string = '{} {}'.format(rand_word(thing), title.string)
      
    # try to replace "url(...)" references in CSS included in the HTML
    style_tags = soup.findAll('style')
    regex = re.compile(r"url\(([a-zA-Z0-9\.\-\/]+)\)")
    # TODO make these images sized right...will need CSS parser
    for tag in style_tags:
      # print(tag.string)
      matches = regex.findall(tag.string)
      for m in matches:
        tag.string = tag.string.replace(m, rand_img_url(thing))
      # print('NEW')
      # print(tag.string)
  
  return soup.encode('utf-8')


def thingify_text(thing, text): 
  """
  Helper function to process strings
  
  Args:
    text (str)
    
  Returns:
    str
  """
  # commenting these out for now, a little too unsubtle
  # text = text.replace('the', 'the goat')
  # text = text.replace('The', 'The goat')
  # text = text.replace(' a ', ' a goat ')
  # text = text.replace('. A ', '. A goat ')
  
  if text[:3].lower() != 'the':
    text = '{} {}'.format(rand_word(thing), text)
  return text


def debug_scrape(url_to_scrape, omit_headers=False):
  """
  Helper function to debug scraping. Returns website html
  without processing. Optionally omit headers to view
  html without dynamic scripts and other stuff from source.
  
  Args:
    url_to_scrape (str): e.g. https://www.wikipedia.org
    [omit_headers] (bool): if True, return html without headers
    
  Returns:
    str
  """
  soup = get_soup(url_to_scrape);
  if omit_headers:
    head = soup.find('head')
    if head: head.extract();
  return soup.encode('utf-8')