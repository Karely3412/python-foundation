"""

1. iter_obj: The iterable object that will be split. (Required)
2. start: The start index. Negative numbers are valid. Default=1
    - For Loop 
    - Start parameter
    - Conditional

3. stop: The stop index. Remember that the slice will end before the stop index. Default = None
4. step: The step direction and magnitude as a positive or negative integer. Default=1

"""



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def slice(iter_obj, start, stop):
    # print(iter_obj)
    sliced_list = []
    # print(start)
    iter_obj_start = iter_obj[start]-1

    for i in iter_obj:
        if i >= start and i <= stop:
            print(i)

        

        

        
        
            
            

        





    # return iter_obj


slice(nums, 5, 8)




# print(slice(my_list))


# print( nums[1:-2:-1] )
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
