import time
from collections import OrderedDict


class Cache(object):
    def __init__(self, max_capacity, expiration=None):
        self.max_capacity = max_capacity
        self.expiration = expiration
        self.values = {}
        self.access_order = OrderedDict()

    def __expired_time(self):
        curr_time = time.time()
        for key, access_time in self.access_order.items():
            if access_time + self.expiration <= curr_time:
                del self.values[key]
                del self.access_order[key]

    def __getitem__(self, key):
        if self.expiration:
            self.__expired_time()
        if key in self.values:
            del self.access_order[key]
            self.access_order[key] = time.time()
            return self.values[key]
        return None

    def __contains__(self, key):
        if self.expiration:
            self.__expired_time()
        return key in self.values

    def __insertitem(self, key, value):
        if key in self.values:
            del self.access_order[key]
        self.access_order[key] = time.time()
        self.values[key] = value

    def __setitem__(self, key, value):
        if self.expiration:
            self.__expired_time()

        if len(self.values) == self.max_capacity:
            old_key, old_timestamp = self.access_order.popitem(last=False)
            del self.values[old_key]
        self.__insertitem(key, value)

    def __delete__(self, key):
        if key in self.values:
            del self.values[key]
            del self.access_order[key]

    def size(self):
        if self.expiration:
            self.__expired_time()

        return len(self.values)

    def capacity(self):
        return self.max_capacity
