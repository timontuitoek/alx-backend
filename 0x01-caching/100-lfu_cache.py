#!/usr/bin/env python3

"""
Module for implementing an LFU caching system.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.

    Implements the LFU (Least Frequently Used).
    """

    def __init__(self):
        """
        Initializes the LFUCache instance.
        """
        super().__init__()
        self.freq_count = {}  # Dict to track key usage frequency

    def put(self, key, item):
        """
        Assigns the item value for the key key.

        Implements LFU eviction policy and uses LRU if necessary.

        Args:
            key: The key to be assigned.
            item: The value to be assigned.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq_count.values())
                lfu_keys = [k for k, v
                            in self.freq_count.items() if v == min_freq]
                lru_key = min(lfu_keys, key=lambda k: self.cache_data[k][1])
                del self.cache_data[lru_key], self.freq_count[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = (item, 0)
            self.freq_count[key] = 0

    def get(self, key):
        """
        Returns the value linked to the given key.

        Updates key usage frequency.

        Args:
            key: The key to retrieve the value.

        Returns:
            The value associated with the key,
            or None if key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        value, freq = self.cache_data[key]
        self.freq_count[key] += 1
        return value
