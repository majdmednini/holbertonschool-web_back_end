#!/usr/bin/env python3
'''
Return a tuple containing the start and end index
'''


def index_range(page, page_size):
    '''
    Return a tuple containing the start and end index
    '''

    end_of_index = page * page_size
    start_of_index = end_of_index - page_size

    return (start_of_index, end_of_index)
