from gumballMachine import GumballMachine
from gumballMonitor import GumballMonitor


class GumballMachineTestDrive:
    def test(self, location, count):
        gumballMachine = GumballMachine(location, count)

        gumballMonitor = GumballMonitor(gumballMachine)
        gumballMonitor.report()


if __name__ == '__main__':
    GumballMachineTestDrive().test("Seattle", 112)
