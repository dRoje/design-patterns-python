from turkey import Turkey
from duck import Duck


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        # type: (Turkey) -> None
        assert isinstance(turkey, Turkey)
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for x in range(5):
            self.turkey.fly()


