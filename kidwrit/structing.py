import string
from transliterate import translit, get_available_language_codes
import os


class Logfile:
    def __init__(self, name):
        self.name = log_heading(name)

    def mk_note(self, info: str):
        with open(self.name, 'w') as f:
            f.write(info)


def log_heading(s: str):
    s1 = s.translate(str.maketrans('', '', string.punctuation))
    print(f"translated s: _{s1}_")
    s2 = s1.replace(" ", '')
    print(f"stripped s: _{s2}_")
    s3 = translit(s2, "ru", reversed=True)
    print(s3)
    return s3+".txt"


def log_directory():
    # Directory
    directory = "logs"
    # Parent Directory path
    parent_dir = os.getcwd()
    # Path
    path = os.path.join(parent_dir, directory)
    # Create the directory
    if not os.path.exists(path):
        os.mkdir(path)
    return path

