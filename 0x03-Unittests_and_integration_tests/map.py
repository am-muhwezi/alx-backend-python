#!/usr/bin/env python3


def to_upper_case(s):
    return(s).upper()
    
def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line


map_iterator = map(to_upper_case, (1, 'a', 'abc'))
print_iterator(map_iterator)