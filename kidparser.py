import _io
import re
from bs4 import BeautifulSoup
import kidwrit


def parse_kid(soup: BeautifulSoup):
    kid_info = ''
    h = soup.find("h1")
    for s in h.find_all("span"):
        kid_info = "".join((kid_info, s.text))
    print("\nPARSE_KIDS\nKid info:", kid_info)
    kid = kidwrit.toss_kid_info(kid_info)
    return kid


def parse_heading(soup: BeautifulSoup, kid: kidwrit.Kid):
    #for child in soup.children: print(child)
    print("hello world")


def toss_soup(contents: str, key: str):
    key = "<" + key
    primary_matches = re.split(f"({key})", contents)
    primary_matches.pop(0)
    [primary_matches.remove(m) for m in primary_matches if m == key]
    matches = [key+m for m in primary_matches]
    print(f"\n-TOSS_SOUP---\nkey: {key}\nlen(matches): {len(matches)}\n-------------")
    return matches
