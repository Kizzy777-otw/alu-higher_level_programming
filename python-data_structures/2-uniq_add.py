#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list"""
    unique_nums = []
    total = 0
    for num in my_list:
        if num not in unique_nums:
            unique_nums.append(num)
            total += num
    return total
