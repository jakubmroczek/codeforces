##!/usr/bin/env python3
from test_a import tests

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

def test(tests):
    return ["YES"  if solve(test) else "NO" for test in tests]

def main():
    number_of_cases = int(input())
    for i in range(number_of_cases):
        array_len = int(input())
        array = list(input())
        array.remove(" ")
        array = [int(n) for n in array]

if __name__ == '__main__':
    # print(test(tests))
    main()


