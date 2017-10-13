class GumballMachine:
    def __init__(self, count):
        # type: (int) -> None
        from states import SoldOutState, NoQuarterState, HasQuarterState, SoldState, WinnerState
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)

        self.state = self.soldOutState
        self.count = count
        if self.count > 0:
            self.state = self.noQuarterState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state):
        self.state = state

    def getCount(self):
        return self.count

    def getSoldState(self):
        return self.soldState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldOutState(self):
        return self.soldOutState

    def getWinnerState(self):
        return self.winnerState

    def releaseBall(self):
        print "A gumball comes rolling out the slot"
        if self.count != 0:
            self.count -= 1

    def __str__(self):
        result = ""
        result += "\nMighty Gumball, Inc."
        result += "\nJava-enabled Standing Gumball Model #2004\n"
        result += "Inventory: " + str(self.count) + " gumball"
        result += "\nMachine is "
        if self.state == self.soldOutState:
            result += "sold out"
        elif self.state == self.noQuarterState:
            result += "waiting for quarter"
        elif self.state == self.hasQuarterState:
            result += "waiting for turn of crank"
        elif self.state == self.soldState:
            result += "delivering a gumball"
        result += "\n"
        return result

    def refill(self, count):
        # type: (int) -> None
        self.count = count
        self.state = self.noQuarterState


