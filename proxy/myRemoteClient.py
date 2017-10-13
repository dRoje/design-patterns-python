import Pyro4


class MyRemoteClient:
    def __init__(self):
        pass

    def go(self):
        uri = "PYRO:example.myRemote@localhost:32865"
        service = Pyro4.Proxy(uri)

        s = service.sayHello()
        #
        # print s


if __name__ == '__main__':
    MyRemoteClient().go()

