from multiprocessing import Process
from multiprocessing.managers import BaseManager
import time
from realThing import RealThing
from realThingProxy import RealThingProxy
from otherProcess import infiniteLoop


class MyManager(BaseManager):
    pass


MyManager.register('RealThing', RealThing, RealThingProxy)


if __name__ == '__main__':
    manager = MyManager()
    manager.start()

    realThing = manager.RealThing()


    p1 = Process(target=infiniteLoop, args=[realThing])

    print "-----------------"
    print "Calling function from main process: "
    realThing.myFunc()
    realThing.setValue(2)
    print realThing.getValue()
    p1.start()
    while True:
        time.sleep(1)
        print "realThing: " + str(realThing.myValue)
        realThing.myValue = realThing.myValue + 1

