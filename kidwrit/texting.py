import re

from kidwrit import kidding


class KidText:
    def __init__(self, name: str, place: str, date: str, creator: kidding.Kid, grade=None, text=None):
        self.name = name
        self.place = place
        self.date = date
        self.text = text
        self.creator = creator
        if grade is None:
            print("Default constructor called: no grade")
        else:
            self.grade = grade
            print("Parameterized constructor called with grade", self.grade)
        if text is None:
            print("Default constructor called: no text")
        else:
            self.text = text
        # probably later i'll add a KidAnno list


def toss_heading(info: str, creator: kidding.Kid):
    print(f"\n-TOSS_HEADING---\n1) Info: {info}")
    date = re.search(r'\d\d.\d\d.\d\d\d\d', info).group()
    print("2) Date: ", date)
    bits = info.split(date)
    print(f"3) Bits: {bits}")
    name = bits[0].strip()
    place = bits[1].strip()
    print(f"4) Text place: {place}")
    print("----------------")
    heading = KidText(name=name, date=date, place=place, creator=creator)
    return heading
