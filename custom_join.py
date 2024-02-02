
def cust_join(it_obj, separ):
    index_of_list = range(len(it_obj))
    str_list = ''

    for i in index_of_list:
        if i == index_of_list[-1]:
            it_obj_str1 = f'{it_obj[i]}'
            str_list += it_obj_str1
        else:
            it_obj_str2 = f'{it_obj[i]}{separ}' 
            str_list += it_obj_str2
            
    
    return str_list


print(cust_join(["Apple","Banana",15,17.6,"Orange", "Orange"], ','))




# def cust_join(it_obj, separ):
#     index_of_list = range(len(it_obj))

#     for i in index_of_list:
#         if i == len(it_obj) - 1:
#             it_obj_str = f'{it_obj[i]}'
#             print(it_obj_str, end='')
#         else:
#             it_obj_str = f'{it_obj[i]}{separ}' 
#             print(it_obj_str, end='')


# cust_join(["Apple","Banana",15,17.6,"Orange", "Orange"], ',')