from kidwrit.texting import KidText


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

