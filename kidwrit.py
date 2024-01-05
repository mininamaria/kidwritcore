
import re

class Kid:
    def check_b_date(self):
        if self.b_date == 'ok':
            return True
        else:
            return False

    def __init__(self, name: str, b_date: str):
        self.name = name
        self.b_date = b_date
        if not self.check_b_date():
            # throw a good ol'Exception on 'em
            print("go fuck yourself: age exception")


class KidText:
    def __init__(self, name: str, place: str, grade: int, text: str, creator: Kid, url: str):
        self.name = name
        self.place = place
        self.grade = grade
        self.text = text
        self.creator = creator
        self.url = url

    def t_parse(self):
        return self.name+"is hell"


class Annotation:
    def a_spans(self):
        return 1, (self.quote.split())

    def a_offsets(self):
        #   ТАК НЕ РАБОТАЕТ! спросить у ЯЭ
        start_offset = self.document.find(self.quote)
        end_offset = start_offset + len(self.quote)
        return start_offset, end_offset

    def a_parse_data(self):
        spans = self.a_spans()
        offsets = self.a_offsets()
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
