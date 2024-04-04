#!/usr/bin/env python3
"""
Module for implementing a LIFO caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.

    This caching system implements the LIFO
    (Last In, First Out) eviction policy.
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value for the key key.

        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        it discards the last item put in cache
        (LIFO algorithm) and prints DISCARD with the key discarded.

        Args:
            key: The key to be assigned.
            item: The value to be assigned.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the last item added to the cache (LIFO)
                last_item_key = next(reversed(self.cache_data))
                del self.cache_data[last_item_key]
                print("DISCARD:", last_item_key)
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


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    print(my_cache.get("A"))  # Output: Hello
    my_cache.put("D", "School")  # Discards "Holberton"
    print(my_cache.get("C"))  # Output: None
    print(my_cache.get("D"))  # Output: School
