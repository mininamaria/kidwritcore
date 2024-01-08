import requests
from pprint import pprint
from bs4 import BeautifulSoup
import kidwrit
import kidparser

'''
response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()
'''
with open('for_proga.html', "r") as f:
    plates = kidparser.toss_soup(f.readline(), 'h1')
    print("\nPlates (h1): (too long)")
    for plate in plates:
        soup = BeautifulSoup(plate, 'html.parser')
        spoons = kidparser.toss_soup(plate, 'h2')
        kid = kidparser.parse_kid(soup)
        print("\nSpoons (h2): (too long)")
        for spoon in spoons:
            #  для каждой ложки у нас уже есть ребёнок!
            kidparser.parse_heading(soup, kid)
    #  kid_info.
    # print(kid_info)
    # for k in kids: print("Kid:", k.to_string())
    #  pprint(soup)
