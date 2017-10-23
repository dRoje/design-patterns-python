from realThing import RealThing
import time


def infiniteLoop(realThingProxy):
    # type: (RealThing) -> None
    while True:
        time.sleep(1)
        if realThingProxy.myValue == 5:
            print "Reseting value of realThing via Proxy"
            realThingProxy.myValue = 0
