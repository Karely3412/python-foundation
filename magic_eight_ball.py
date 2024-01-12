import random

# def magic_8_ball():
#     user_prompt = input("Ask a question: ")
#     rand = random.randrange(1,9)

#     if user_prompt == '':
#         return ("Program ended")
    
#     if rand == 1:
#         return ("Outlook good!")
#     elif rand == 2:
#         return ("You may rely on it!")
#     elif rand == 3:
#         return ("Ask aganlater!")
#     elif rand == 4:
#         return ("Concentae and ask again!")
#     elif rand == 5:
#         return ("Reply hz, try again!")
#     elif rand == 6:
#         return ("My repl s no!")
#     elif rand == 7:
#         return ("It's certain!")
#     elif rand == 8:
#          return ("My sources say no!")
    
# print(magic_8_ball())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   


# def magic_8_ball():
#     user_prompt = input("Ask a question: ")
#     rand = random.randrange(1,9)

#     if user_prompt == '':
#         return ("Program ended")
    
#     else:
#         if rand == 1:
#             return ("Outlook good!")
#         elif rand == 2:
#             return ("You may rely on it!")
#         elif rand == 3:
#             return ("Ask aganlater!")
#         elif rand == 4:
#             return ("Concentae and ask again!")
#         elif rand == 5:
#             return ("Reply hz, try again!")
#         elif rand == 6:
#             return ("My repl s no!")
#         elif rand == 7:
#             return ("It's certain!")
#         elif rand == 8:
#             return ("My sources say no!")
    
# print(magic_8_ball())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   


# def magic_8_ball():
#     user_prompt = input("Ask a question: ")
#     rand = random.randrange(1,9)

#     if user_prompt:
    
#         if rand == 1:
#             return ("Outlook good!")
#         elif rand == 2:
#             return ("You may rely on it!")
#         elif rand == 3:
#             return ("Ask aganlater!")
#         elif rand == 4:
#             return ("Concentae and ask again!")
#         elif rand == 5:
#             return ("Reply hz, try again!")
#         elif rand == 6:
#             return ("My repl s no!")
#         elif rand == 7:
#             return ("It's certain!")
#         elif rand == 8:
#             return ("My sources say no!")
    
#     else:
#         return ("Program ended")


# print(magic_8_ball())


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# def magic_8_ball():
#     user_prompt = input("Ask a question: ")

#     list_answers = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]

#     rand = random.randrange(0,8)

#     if user_prompt:
#         print(list_answers[rand])

#     return rand


# magic_8_ball()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


def magic_8_ball():
    user_prompt = input("Ask a question: ")

    list_answers = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]
    
    if user_prompt == '':
        print ("Program ended! Come back again soon!")
    
    else: 
        print (random.choice(list_answers))

    
magic_8_ball()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# def magic_8_ball():
#     user_prompt = input("Ask a question: ")

#     list_answers = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]
    
#     if user_prompt == '':
#         return "Program ended! Come back again soon!"
    
#     else: 
#         return random.choice(list_answers)

    


# print(magic_8_ball())