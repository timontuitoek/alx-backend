#!/usr/bin/env python3
"""Module for implementing a basic caching system."""


class BaseCaching:
    """
    BaseCaching class as a base for caching systems.
    """
    MAX_ITEMS = 10


    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        """
        Prints the current cache data.
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
