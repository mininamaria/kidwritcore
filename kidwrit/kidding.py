import re


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

