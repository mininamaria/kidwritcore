import re


def toss_kid_info(info: str):
    print(f"\n-TOSS_KID_INFO---\n1) Info: {info}")
    b_year = re.search(r'\d\d\d\d', info).group()
    print("2) B_year: ", b_year)
    bits = info.split(b_year)
    # re.sub(b_year, info, '#')
    # bits = info.split('#')
    print(f"3) Bits: {bits}")
    name = bits[0].strip()
    gndr = bits[1].strip()
    if gndr == 'ж':
        gender = "женский"
    elif gndr == 'м':
        gender = "мужской"
    else:
        gender = '-'
    kid = Kid(name, b_year, gender)
    print(f"4) Kid: {kid.to_string()}")
    print("------------------")
    return kid


class Kid:
    def check_b_year(self):
        #  if self.b_year == 'ok':
        if self.b_year is None or not re.fullmatch(r'\d\d\d\d', self.b_year):
            # throw a good ol'Exception on 'em
            print("go fuck yourself: age exception")
            return False
        else:
            return True

    def __init__(self, name: str, b_year: str, gender: str):
        self.name = name
        self.b_year = b_year
        self.gender = gender

    def to_string(self):
        return f"[name: {self.name}, b_year: {self.b_year}, gender: {self.gender}]"


class KidText:
    def __init__(self, name: str, place: str, grade: int, text: str, creator: Kid, url: str):
        self.name = name
        self.place = place
        self.grade = grade
        self.text = text
        self.creator = creator
        self.url = url

    def parse(self):
        return self.name + "is hell"


class KidAnno:
    def spans(self):
        return 1, (self.quote.split())

    def offsets(self):
        #   ТАК НЕ РАБОТАЕТ! спросить у ЯЭ
        start_offset = self.document.find(self.quote)
        end_offset = start_offset + len(self.quote)
        return start_offset, end_offset

    def a_parse_data(self):
        spans = self.spans()
        offsets = self.offsets()
        ranges = [{"start": f"/span[{spans[0]}]",
                   "end": f"/span[{spans[1]}]",
                   "startOffset": offsets[0],
                   "endOffset": offsets[1]}]
        return {"ranges": ranges, "quote": self.quote,
                "text": self.text, "tags": self.tags}

    def __init__(self, document: str, quote: str, text: str, tags: list, parent: KidText):
        """
        :param document: sentence containing the mistake
        :param quote: text fragment with the mistake
        :param text: comment text
        :param tags: mistake categories
        """
        self.document = document
        self.quote = quote
        self.text = text  # comment
        self.tags = tags
        self.parent = parent
