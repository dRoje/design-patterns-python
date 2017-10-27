class Message:
    def __init__(self, function, args=None):
        # type: (str, list) -> None
        assert type(function) is str
        self.function = function
        if args is None:
            args = []
        assert type(args) is list
        self.args = args

    def getFunction(self):
        # type: () -> str
        return self.function

    def getArgs(self):
        # type: () -> list
        return self.args


