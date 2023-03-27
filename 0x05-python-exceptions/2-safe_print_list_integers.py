#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        print(my_list[i] for i in range(x))
        count += 1
    except (ValueError, IndexError):
        pass
