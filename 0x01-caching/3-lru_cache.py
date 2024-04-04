#!/usr/bin/env python3

"""
Module for implementing an LRU caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.

    This caching system implements the LRU
    (Least Recently Used) eviction policy.
    """

    def __init__(self):
        """
        Initializes the LRUCache instance.
        """
        super().__init__()
        self.order = []  # List to maintain the order of key usage

    def put(self, key, item):
        """
        Assigns the item value for the key key.

        If the key already exists in the cache,
        the value is updated.

        Otherwise, a new entry is created and the least
        recently used key is discarded if necessary.

        Args:
            key: The key to be assigned.
            item: The value to be assigned.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.order.pop(0)  # Get the least recently used key
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Returns the value linked to the given key.

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
