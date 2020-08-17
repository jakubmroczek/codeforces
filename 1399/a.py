##!/usr/bin/env python3
def solve(array):
    '''
        Returns True if an array can be reduced to a single element following
        the 1399A task or False otherwise.
    '''
    if len(array) == 1:
        return True

    array.sort()

    for index in range(0, len(array) - 1):
        left, right = array[index], array[index + 1]
        if abs(left - right) > 1:
            return False

    return True

number_of_cases = int(input().strip())
for i in range(number_of_cases):
    try:
        array_len = int(input().strip())

        array = list(input().split())
        array = [int(n) for n in array if (n != " " or n != "")]
        if solve(array):
            print("YES")
        else:
            print("NO")
    except Exception as e:
        print(f'{e}')
