#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 03:44:16 2018

@author: aman
"""

import os
import time
import urllib
from bs4 import BeautifulSoup

# Print waiting message
print('Retrieving scores...')


while True:
    # cricinfo website
    cricbuzz = 'http://www.cricbuzz.com/'

    # query the website and return the html to variable 'page'
    page = urllib.request.urlopen(cricbuzz)
    
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    
    # Retrieve the scores from html
    name_box = soup.find_all('div', attrs={'class' : 'cb-col cb-col-25 cb-mtch-blk'})
    
    # Clear the terminal
    os.system('clear')
    
    for i in name_box:
        name = i.text.strip()
        print(name)
        print()
        
    # Wait 50s before refreshing
    time.sleep(50)
