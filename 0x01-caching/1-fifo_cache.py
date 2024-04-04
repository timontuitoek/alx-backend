#!/usr/bin/env python3
"""
Module for implementing a FIFO caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.

    This caching system implements the FIFO (First In,
    First Out) eviction policy.
    """

    def __init__(self):
        """
        Initializes the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value for the key key.

        If the number of items in self.cache_data is
        higher than BaseCaching.MAX_ITEMS,
        it discards the first item put in cache
        (FIFO algorithm) and prints DISCARD with the key discarded.

        Args:
            key: The key to be assigned.
            item: The value to be assigned.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the first item added to the cache (FIFO)
                first_item_key = next(iter(self.cache_data))
                del self.cache_data[first_item_key]
                print("DISCARD:", first_item_key)
            self.cache_data[key] = item

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
        return self.cache_data[key]
