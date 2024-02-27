def bin_to_dec(bin_str):
    dec_str = 0
    multi = 1

    for i in reversed(bin_str):
        if i == '1':
            dec_str += multi
        multi = multi *2

    return dec_str
            

    
  
print(bin_to_dec("11111111"))
print(bin_to_dec("11011001"))
print(bin_to_dec("10101011"))

"""
TESTING:
128 64 32 16 8 4 2 1
1   1  0  1  1 0 0 1

"""