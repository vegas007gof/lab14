#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def convert(type: str):
    def activate(nums: str):
        if type == 'list':
            return list(map(int, nums.split(' ')))
        if type == 'tuple':
            return tuple(map(int, nums.split(' ')))

    return activate


if __name__ == '__main__':
    print(f"List: {convert('list')('1 2 3 4 5 6')}\n"
          f"Tuple: {convert('tuple')('1 2 3 4 5 6')}")