#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:25:26 2018

@author: aman
"""

import os
import time
import urllib
from bs4 import BeautifulSoup


def show_score(page, n):
    print('Retrieving score..')
    
    while True:
        soup = get_soup(page)
        match_box = soup.find_all('div', attrs={'class' : 'cb-col cb-col-25 cb-mtch-blk'})
        
        os.system('clear')
        
        if n == 0 :
            for match in match_box:
                score = match.text.strip()
                print(score)
                print()
        else:
            score = match_box[n - 1].text.strip()
            print(score)
            
        time.sleep(50)


def print_match_list(soup) :
    count = 0
    print(str(count) + ' : ' + 'Show all matches')
    
    match_box = soup.find_all('div', attrs={'class' : 'cb-col cb-col-25 cb-mtch-blk'})
    
    for match in match_box:
        count += 1
        print(str(count) + ' : ' + match.a.get('title'))
        
    

def get_soup(page):
    # query the website and return the html to variable 'page'
    page = urllib.request.urlopen(page)
    
    # parse the html using beautiful soup and return it
    return BeautifulSoup(page, 'html.parser')


def run_tricket(page):
    print('Retrieving matches...')
    
    soup = get_soup(page)
    
    print_match_list(soup)
    
    print()
    
    option = input('Enter your choice: ')
    
    show_score(page, int(option))
        

if __name__ == "__main__":
    run_tricket('http://www.cricbuzz.com/')
