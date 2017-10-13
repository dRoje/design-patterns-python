import Pyro4
import Pyro4.errors
from abc import ABCMeta


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class MyRemote:
    __metaclass__ = ABCMeta

    def sayHello(self):
        # type: () -> str
        raise Pyro4.errors.CommunicationError


