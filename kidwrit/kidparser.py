import re
from bs4 import BeautifulSoup

import texting
from kidwrit import kidding


def parse_kid(soup: BeautifulSoup):
    kid_info = ''
    h = soup.find("h1")
    for s in h.find_all("span"):
        kid_info = "".join((kid_info, s.text))
    print("\nPARSE_KIDS\nKid info:", kid_info)
    kid = kidding.toss_kid_info(kid_info)
    return kid


def parse_heading_info(soup: BeautifulSoup, kid: kidding.Kid):
    heading = ''
    texts = []
    h2 = soup.find_all("h2")
    for h in h2:
        for s in h.find_all("span"):
            heading = "".join((heading, s.text))
        print("\nPARSE_HEADINGS\nText heading:", heading)
        # for child in soup.children: print(child)
        print("hello world")
        text = texting.toss_heading(heading, kid)
        #   here we'll add text data
        texts.append(text)
        heading = ''
    return texts


def toss_soup(contents: str, key: str):
    key = "<" + key
    primary_matches = re.split(f"({key})", contents)
    primary_matches.pop(0)
    [primary_matches.remove(m) for m in primary_matches if m == key]
    matches = [key+m for m in primary_matches]
    print(f"\n-TOSS_SOUP---\nkey: {key}\nlen(matches): {len(matches)}\n-------------")
    return matches




'''
    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")
'''


