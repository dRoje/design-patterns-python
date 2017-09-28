###
# MULTI THREADING
###
# import threading
# class SingletonMixin(object):
#     __singleton_lock = threading.Lock()
#     __singleton_instance = None
#
#     @classmethod
#     def instance(cls):
#         if not cls.__singleton_instance:
#             with cls.__singleton_lock:
#                 if not cls.__singleton_instance:
#                     cls.__singleton_instance = cls()
#         return cls.__singleton_instance

###
# MULTIPROCESSING
# Best is to designate one specific process as owning that instance and dedicated to it; any other process requiring
# access to that instance obtains it by sending messages to the owning process via a Queue (as supplied by the
# multiprocessing module) or other IPC mechanisms for message passing, and gets answers back via similar mechanisms.
###


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ChocolateBoiler:
    __metaclass__ = Singleton

    def __init__(self):
        self.empty = True
        self.boiled = False

    def fill(self):
        if self.isEmpty():
            self.empty = False
            self.boiled = False
            # fill up boiler

    def drain(self):
        if not self.isEmpty() and self.isBoiled():
            self.empty = True
            # drain the boiler

    def boil(self):
        if not self.isBoiled() and not self.isEmpty():
            self.boiled = True
            # boil the contents

    def isEmpty(self):
        return self.empty

    def isBoiled(self):
        return self.boiled



chocolateBoiler1 = ChocolateBoiler()
chocolateBoiler2 = ChocolateBoiler()
print chocolateBoiler1
print chocolateBoiler2