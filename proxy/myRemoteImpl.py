from myRemote import MyRemote
import Pyro4


class MyRemoteImpl(MyRemote):
    def sayHello(self):
        # type: () -> str
        return "Hey"


def main():
    Pyro4.Daemon.serveSimple(
        {
            MyRemote: "example.myRemote"
        },
        ns=False)


if __name__ == '__main__':
    service = MyRemoteImpl
    main()
