#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    returned_list = []
    for num in my_list:
        if num % 2 == 0:
            returned_list.append(True)
        else:
            returned_list.append(False)
    return(returned_list)
