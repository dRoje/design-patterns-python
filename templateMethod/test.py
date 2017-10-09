from coffee import CoffeeWithHook


class BeverageTestDrive:
    def test(self):
        coffeeHook = CoffeeWithHook()

        print "making coffee..."
        coffeeHook.prepareRecipe()


if __name__ == '__main__':
    BeverageTestDrive().test()