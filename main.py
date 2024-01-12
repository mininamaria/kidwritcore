import sys

from bs4 import BeautifulSoup

import kidwrit.kidparser
from kidwrit import kidparser

'''
response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()
'''

with open('kids_full.html', "r") as f:
    plates = kidparser.toss_soup(f.readline(), 'h1')
    for plate in plates:
        soup = BeautifulSoup(plate, 'html.parser')
        spoons = kidparser.toss_soup(plate, 'h2')
        kid = kidparser.parse_kid(soup)
        for spoon in spoons:
            print(f"\nSpoon: {spoon}")
            kidparser.parse_heading_info(soup, kid)
            drops = kidparser.toss_soup(spoon, 'p')
            for drop in drops:
                print("\nDrop:", drop)
                kidwrit.kidparser.parse_text(BeautifulSoup(drop, 'html.parser'))
    #  kid_info.
    # print(kid_info)
    # for k in kids: print("Kid:", k.to_string())
    #  pprint(soup)
