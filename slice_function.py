"""

1. iter_obj: The iterable object that will be split. (Required)
2. start & stop: The start index. Negative numbers are valid. Default=1
    - For Loop 
    - Conditional
        - Start & stop parameter with Arithmetic Operators

3. stop: The stop index. Remember that the slice will end before the stop index. Default = None
4. step: The step direction and magnitude as a positive or negative integer. Default=1
START & STOP:
    - if we have -start then start need to start at end of list

STEP:


"""

#       0  1  2  3  4  5  6  7  8 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#      -9 -8 -7 -6 -5 -4 -3 -2 -1


#       0  1  2  3  4
# nums = [1, 2, 3, 4, 5]
#      -5 -4 -3 -2 -1


def slice(iter_obj, start, stop, step):
    sliced_list = []
    stepped_list = []

    if start < 0:
       start += len(nums)

    if stop < 0:
       stop += len(nums)

    if start > stop and step < 0:
        temp = start + 1
        start = stop + 1
        stop = temp

    # 6 - 2 -2

    if (start < stop and stop < 0) and not (start==0 and stop==len(iter_obj)):
        return []


    for idx, val in enumerate(iter_obj):
        if idx >= start and idx < stop:
            sliced_list.append(val)
    

    if step < 0:
        sliced_list.reverse()


    for idx, val in enumerate(sliced_list):
        if idx % step == 0:
            stepped_list.append(val)
        

    return stepped_list


print(slice(nums, -1, 4, -1))
print(       nums[-1: 4: -1] )

# print('+++')
# print('-++')
# print('+-+')
# print('++-')
# print('---')

# print(slice(nums, -1, -4, -1))
# print(       nums[-1: -4: -1] )



# print(slice(my_list))


# print( slice(nums, 1, -2, -1) )



# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# output = slice(nums, 2, -2)

# print(output)

# # Output
# # [3, 4, 5, 6, 7]

# ## Example 2
# print( slice(nums, stop = 4) )

# # Output
# # [1, 2, 3, 4]

# ## Example
# print( slice(nums, step=-1) )

# Output
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
