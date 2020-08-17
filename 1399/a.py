##!/usr/bin/env python3

def _sort(array):
    array.sort();

def solve(array):
'''
    Returns True if an array can be reduced to a single element following
    the 1399A task or False otherwise.
'''
    if len(array) == 1:
        return True

    _sort(array)

    for index in range(0, len(array) - 1):
        left, right = array[index], array[index + 1]
        if abs(left - right) > 1:
            return False

    return True

if __name__ == '__main__':
    main()
