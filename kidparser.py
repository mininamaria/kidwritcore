import _io
import re
from bs4 import BeautifulSoup
import kidwrit


def parse_kids(soup: BeautifulSoup):
    kid_info = ''
    kids = []
    for h in soup.find_all("h1"):
        for s in h.find_all("span"):
            kid_info = "".join((kid_info, s.text))
        print("Kid info:", kid_info)
        kid = kidwrit.k_toss_info(kid_info)
        print(kid.to_string())
        kids.append(kid)
    return kids


def parse_heading(soup: BeautifulSoup, kid: kidwrit.Kid):
    #for child in soup.children: print(child)
    print("hello world")


def toss_soup(contents: str):
    primary_matches = re.split("(<h1)", contents)
    primary_matches.pop(0)
    [primary_matches.remove(m) for m in primary_matches if m == '<h1']
    matches = ["<h1"+m for m in primary_matches]
    print(f"-TOSS_SOUP---\nlen(matches): {len(matches)}\n-------------")
    return matches


def toss_soup_modified(contents: str, key: str):
    key = "<" + key
    primary_matches = re.split(f"({key})", contents)
    primary_matches.pop(0)
    [primary_matches.remove(m) for m in primary_matches if m == key]
    matches = [key+m for m in primary_matches]
    print(f"-TOSS_SOUP---\nkey = {key}\nlen(matches): {len(matches)}\n-------------")
    return matches
