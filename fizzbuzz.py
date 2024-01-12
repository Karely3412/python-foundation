"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""

def fizzbuzz(number):

    for num in range(1, number):

        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")

        elif num % 3 == 0:
            print("Fizz")

        elif num % 5 == 0:
            print("Buzz")
        
        else:
            print(num)
    

fizzbuzz(101)



# (lambda: [print("FizzBuzz") if i % 3 == 0 and i % 5 == 0 else print("Fizz") if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i) for i in range(1, 101)])()