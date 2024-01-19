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
            self.grade = None
        else:
            self.grade = grade
            print("Parameterized constructor called with grade", self.grade)
        if text is None:
            print("Default constructor called: no text")
            self.text = None
        else:
            self.text = text
        # probably later i'll add a KidAnno list

    def to_string(self):
        return f"TEXT {self.name} by {self.creator.name}:\n- place: {self.place},\n- date: {self.date}," \
               f"\n- grade: {self.grade},\n- text: {self.text}"

    def date_to_ints(self):
        return [int(item) for item in self.date.split('.')]

    def calc_grade(self):
        txt_date = self.date_to_ints()
        if txt_date[2] == self.creator.to_sch_year:
            return 1
        else:
            return txt_date[2]-self.creator.to_sch_year+(txt_date[1]//9)


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







