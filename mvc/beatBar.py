class BeatBar:
    def __init__(self):
        self.value = 0

    def setValue(self, value):
        # type: (int) -> None
        self.value = value

    def getValue(self):
        # type: () -> int
        return self.value
