#!/usr/bin/env python3
"""Module for implementing a basic caching system."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Assigns the item value for the key key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the given key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
