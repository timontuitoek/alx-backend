#!/usr/bin/env python3
"""function index_range"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index
