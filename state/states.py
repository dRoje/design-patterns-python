from state import State
from gumballMachine import GumballMachine
import random


class SoldState(State):
    def __init__(self, gumballMachine):
        # type: (GumballMachine) -> None
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "Please wait for your gumball"

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class NoQuarterState(State):
    def __init__(self, gumballMachine):
        # type: (GumballMachine) -> None
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
        print "You inserted a quarter"

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned but there's no quarter")

    def dispense(self):
        print("You need to pay first")


class HasQuarterState(State):
    def __init__(self, gumballMachine):
        # type: (GumballMachine) -> None
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "You can't insert another quarter"

    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("You turned...")
        winner = random.randrange(0, 10)
        if winner == 0 and self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("No gumball dispensed")


class SoldOutState(State):
    def __init__(self, gumballMachine):
        # type: (GumballMachine) -> None
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "You can't insert a quarter, the machine is sold out"

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")


class WinnerState(State):
    def __init__(self, gumballMachine):
        # type: (GumballMachine) -> None
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "error winner"

    def ejectQuarter(self):
        print "error winner"

    def turnCrank(self):
        print "error winner"

    def dispense(self):
        print("WINNER!!!")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print "Oopse, out of gumballs!"
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

