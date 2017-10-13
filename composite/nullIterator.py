from collections import Iterator

class NullIterator(Iterator):
    def next(self):
        return None

    def hasNext(self):
        return None

