from pancakeMenu import PancakeMenu
from dinerMenu import DinerMenu
from waitress import Waitress


class MenuTestDrive:
    def test(self):
        pancakeHouseMenu = PancakeMenu()
        dinerMenu = DinerMenu()

        waitress = Waitress(pancakeHouseMenu, dinerMenu)

        waitress.printMenu()


if __name__ == '__main__':
    MenuTestDrive().test()



