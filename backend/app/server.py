#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Flask webserver
# TODO: explain stuff here

import os
import traceback
import json

from flask import Flask, request, render_template, jsonify, url_for, redirect

import helpers
import constants

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

###############################
# web app setup
###############################

@app.route('/')
def homepage():
  return render_template('start.html')
  
@app.route('/go', methods=['GET'])
def display_goat_webpage():
  url_to_scrape = request.args.get('input_url', None)
  thing = request.args.get('thing', 'fish')
  if url_to_scrape:
    print('({}) creating webpage for {}...'.format(thing, url_to_scrape))
    
    # serve page directly
    html_data = helpers.thingify(thing, url_to_scrape)
    if not html_data:
      return render_template('error.html', data={
        'error': 'Did you enter a valid URL?', 
        'url': url_to_scrape})

    # return render_template('index.html', data={'html': html_data})
    return html_data
    
    # add layer of error handling
    # try:
    #   html_data = helpers.goatify(url_to_scrape)
    # except Exception as e:
    #   print('something went wrong')
    #   print(e)
    #   return render_template('error.html', data={'error': e, 'url': url_to_scrape})
    # return render_template('index.html', data={'html': html_data})

###############################
# debugging
###############################
@app.route('/debug', methods=['GET'])
def scrape_raw():
  url_to_scrape = request.args.get('input_url', None)
  if url_to_scrape:
    print('DEBUG scraping {}...'.format(url_to_scrape))
    
    # serve page directly
    html_data = helpers.debug_scrape(url_to_scrape)
    # return render_template('index.html', data={'html': html_data})
    return html_data

@app.route('/debug-no-headers', methods=['GET'])
def scrape_raw_without_headers():
  url_to_scrape = request.args.get('input_url', None)
  if url_to_scrape:
    print('DEBUG scraping {}, omitting headers...'.format(url_to_scrape))
    
    # serve page directly
    html_data = helpers.debug_scrape(url_to_scrape, omit_headers=True)
    # return render_template('index.html', data={'html': html_data})
    return html_data

if __name__ == '__main__':
  constants.LINK_DICT = json.loads(os.environ['LINK_DICT'])
  app.run()