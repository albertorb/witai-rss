#encoding: utf8
"""
         NLP Wit.ai client implementation of a news reader
                  By Alberto Rincón Borreguero

      Department of computational sciences and artificial intelligence
                      University of Seville

"""
__author__= "Alberto Rincón Borreguero"

import os
import feedparser
import sqlite3
import csv

from wit import Wit


def say(session_id, response):
    """
    What is going to be send to the user
    """
    print("This is other ", other)
    print('Sending to user...', response)

def send(request, response):
    """
    """
    print(str(response['text']))


def get_url_feed(request):
    """
    Return last item titles for the requested url
    """
    context = request['context']
    entities = request['entities']
    name = entities['name'][0]['value']
    url = 'nothing'
    with open('list.csv', 'r') as f:
        feed_reader = csv.DictReader(f)
        for row in feed_reader:
            if name == row['name']:
                url = row['url']
                break
    context['feed'] = '\n'.join([item['title'] for item in feedparser.parse(url)['items']])
    return context

def update_list(request):
    """
    Adds the url to list of feeds than the bot can consult
    """
    entities = request['entities']
    context = request['context']
    url = entities['url'][0]['value']
    name = entities['name'][0]['value']
    with open('list.csv', 'a') as f:
        feed_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        feed_writer.writerow([name, url])
    return context


actions = {
    'say': say,
    'send': send,
    'get_url_feed': get_url_feed,
    'update_list': update_list,
}

client = Wit(access_token=os.environ['WIT_TOKEN'], actions=actions)

client.interactive()
