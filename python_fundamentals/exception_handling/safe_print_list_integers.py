#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if not isinstance(my_list[i], int) or isinstance(my_list[i], bool):
                continue
            print("{:d}".format(my_list[i]), end="", flush=True)
            count += 1
        except TypeError:
            continue
    print()
    return count
