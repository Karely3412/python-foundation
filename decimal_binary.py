def dec_to_bin(dec_num):
    my_list = [128, 64, 32, 16, 8, 4, 2, 1]
    result = ''

    for i in my_list:
        if dec_num >= i:
            result += '1'
            dec_num -= i
        else: 
            result += '0'
    return result
        

print(dec_to_bin(25))