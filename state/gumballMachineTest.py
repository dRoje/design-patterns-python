from gumballMachine import GumballMachine


class GumballMachineTestDrive:
    def test(self):
        gumballMachine = GumballMachine(5)

        print(gumballMachine)

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()

        print(gumballMachine)

        gumballMachine.insertQuarter()
        gumballMachine.ejectQuarter()
        gumballMachine.turnCrank()

        print(gumballMachine)

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.ejectQuarter()

        print(gumballMachine)

        gumballMachine.insertQuarter()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()

        print(gumballMachine)


if __name__ == '__main__':
    GumballMachineTestDrive().test()
