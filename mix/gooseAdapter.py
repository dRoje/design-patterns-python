from quackable import Quackable
from goose import Goose


class GooseAdapter(Quackable):
    # adapter
    def __init__(self, goose):
        # type: (Goose) -> None
        self.goose = goose

    def quack(self):
        self.goose.honk()


