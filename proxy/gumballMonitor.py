from gumballMachine import GumballMachine


class GumballMonitor:
    def __init__(self, machine):
        # type: (GumballMachine) -> None
        self.machine = machine

    def report(self):
        print "Gumball Machine: " + self.machine.getLocation()
        print "Current Inventory: " + str(self.machine.getCount())
        print "Gumball State: " + str(self.machine.getState())

