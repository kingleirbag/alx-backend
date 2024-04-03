#!/usr/bin/env python3

'''Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Class BasicCache that inherits from BaseCachin and is a caching system
    '''

    def put(self, key, item):
        '''assign to the dictionar thje `item` value for the key `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''

        return self.cache_data.get(key, None)
