# Exsersie
# - - - - - - - - - - - - - - - - - -
name = 'Name'
city = 'City'
state = 'State'
age = 'Age'

name1 = 'Jane'
name2 = 'Fred'
name3 = 'Betsy'

city1 = 'Boston'
city2 = 'Portland'
city3 = 'Orlando'

state1 = 'Massachusetts'
state2 = 'Oregon'
state3 = 'Florida'

age1 = 24
age2 = 31
age3 = 29

dash = '-'

# print(f'{name:<8}{city:<11}{state:<13}{age:>4}')
# print(f'{dash*7} {dash*10} {dash*13} {dash*4}')
# print(f'{name1:<8}{city1:<10}{state1:<13}{age1:>4}')
# print(f'{name2:<8}{city2:<10}{state2:<13}{age2:>4}')
# print(f'{name3:<8}{city3:<10}{state3:<13}{age3:>4}')



def people_info(name, city, state, age):
    dash = '-'
    header = 'Name' + ' '*4 + 'Ctiy' + ' '*10 + 'State' + ' '*10 + 'Age'
    dashes = f'{dash*6}  {dash*12}  {dash*13}  {dash*4}'

    person_name = name
    person_city = city
    person_state = state
    person_age = age

    peeps_info = f'{header}\n{dashes}\n{person_name:<8}{person_city:<14}{person_state:<14}{person_age:>4}'

    return peeps_info
    

print(people_info('Mickey', 'Aniheim', 'Califonia', "100"))




# Name   City       State         Age
# ------ ---------- ------------- ----
# Jane   Boston     Massachusetts  24
# Fred   Portland   Oregon         31
# Betsy  Orlando    Florida        29