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
    plates = kidparser.toss_soup_modified(f.readline(), 'h1')
    print(plates)
    for plate in plates:
        spoons = kidparser.toss_soup_modified(plate, 'h2')
        print(spoons)
        for spoon in spoons:
            soup = BeautifulSoup(spoon, 'html.parser')
            kids = kidparser.parse_kids(soup)
    #  kid_info.
    # print(kid_info)
    for k in kids: print("Kid:", k.to_string())
    #  pprint(soup)
