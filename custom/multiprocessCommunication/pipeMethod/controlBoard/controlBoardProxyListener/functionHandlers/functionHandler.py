from abc import ABCMeta, abstractmethod


class FunctionHandler:
    __metaclass__ = ABCMeta

    def __init__(self, functionName):
        self.functionName = functionName

    def getFunctionName(self):
        # type: () -> str
        return self.functionName

    @abstractmethod
    def handleFunction(self, args): pass
