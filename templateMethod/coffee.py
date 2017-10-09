from caffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def brew(self):
        print "Dripping Coffee through filter"

    def addCondiments(self):
        print "Adding sugar and milk"


class CoffeeWithHook(CaffeineBeverage):
    def brew(self):
        print "Dripping Coffee through filter"

    def addCondiments(self):
        print "Adding sugar and milk"

    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if answer.lower().startswith("y"):
            return True
        else:
            return False

    def getUserInput(self):
        answer = None
        print "Would you like condiments (y/n)?"
        try:
            answer = raw_input()
        except Exception as e:
            print "Error : " + e.message

        if answer is None:
            return "no"

        return answer


