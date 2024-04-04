#!/usr/bin/env python3
"""
Module for implementing an MRU caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.

    This caching system implements the MRU
    (Most Recently Used) eviction policy.
    """

    def __init__(self):
        """
        Initializes the MRUCache instance.
        """
        super().__init__()
        self.order = []  # List to maintain the order of key usage

    def put(self, key, item):
        """
        Assigns the item value for the key key.
        If the key is already in the cache, the value is updated.

        Args:
            key: The key to be assigned.
            item: The value to be assigned.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.order.pop()  # Get the most recently used key
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Returns the value linked to the given key.

        Updates the order to reflect key was recently accessed.

        Args:
            key: The key to retrieve the value.

        Returns:
            The value associated with the key,
            or None if key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update order of key usage to reflect the key was recently accessed
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
