#!/usr/bin/env python3
"""
index range function
"""

import csv
import math
from typing import List, Dict


class Server:
    """server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """dataset indexed by sorting position
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        return a dictionary
        '''
        assert isinstance(index, int) and index < len(self.indexed_dataset())
        next_page = index + page_size
        data = []
        for elem in range(index, next_page):
            if not self.indexed_dataset().get(elem):
                elem += 1
                next_page += 1
            data.append(self.indexed_dataset()[elem])
        return {'index': index, 'next_index': next_page,
                'page_size': len(data), 'data': data
                }
