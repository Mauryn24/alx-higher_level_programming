#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if idx < 0 or idx > n - 1:
        return my_list
    else:
        return del(my_list)
