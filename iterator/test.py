from pancakeMenu import PancakeMenu
from dinerMenu import DinerMenu
from cafeMenu import CafeMenu
from waitress import Waitress


class MenuTestDrive:
    def test(self):
        pancakeHouseMenu = PancakeMenu()
        dinerMenu = DinerMenu()
        cafeMenu = CafeMenu()

        waitress = Waitress([pancakeHouseMenu, dinerMenu, cafeMenu])

        waitress.printMenu()


if __name__ == '__main__':
    MenuTestDrive().test()



