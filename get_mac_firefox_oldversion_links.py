import json
import requests
import re
import codecs
import csv

def get_links():
    url = 'https://firefox.en.uptodown.com/mac/old'
    print url
    response = requests.get(url).content
    pattern = re.compile(r"//firefox.en.uptodown.com/mac/download/([0-9]+)", re.DOTALL)
    
    base = 'http://firefox.en.uptodown.com/mac/download/'
    m = re.findall(pattern, response)
    for n in m:
        print base + n

get_links()
