

# try:
#   print(10 + '5')

# except:
#   print('Something went wrong')


# try:
#   name = input('Enter your namae:')
#   year_born = input('Enter your year of birth:')
#   age = 2023 - int(year_born)
#   print(f'Hello {name}, you are {age} years old.')

# except TypeError:
#   print('TypeError: Please enter a valid year of birth.')
# except ValueError:
#   print('Value error occured: Please enter a valid year of birth.')



#Unpacking 

# def sum_of_five_nums(a , b, c, d, e):
#     return a + b + c + d + e

# lst = [1,2,3,4,5]
# print(sum_of_five_nums(*lst))



# numbers = range(1, 11)
# print(list(numbers))

# args = [2, 7 , 6]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(list(numbers))  


#unpacke tupls

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# fin , sw , nor , *rest = countries
# print(fin, sw, nor, rest) 


# numbers = [1, 2, 3, 4, 5, 6, 7]
# one , *middle , last = numbers
# print(one, middle, last)


# def unpacking_person_info(name, country, city , age ):
#    return f'{name} lives is {country} , {city}. heis {age}'

# dct = {'name': 'sol' , 'country' :'ethio' , 'city': 'AA' , 'age':23}

# print(unpacking_person_info(**dct))


# def sum_all(*args):
#   s = 0
#   for i in args:
#     s += i
#   return s

# print(sum_all(1, 2, 3, 4, 5, 8))  # Output: 15
# print(sum_all(10, 20, 30))  # Output: 60



# def packing_person_info(**Kwargs):
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")#




#  Spreading in Python

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst = [0,*lst1, *lst2]

# print(lst)  # Output: [0, 1, 2, 3, [4, 5, 6]]

# country_lst1 = ['finland', 'sweden', 'norway'
#                 ]
# country_lst2 = ['denmark', 'iceland', 'greenland']
# country_lst = ['ethiopia', *country_lst1, *country_lst2]
# print(country_lst)  


#Enumerate

# for index , item in enumerate(['a', 'b', 'c']):
#     print(index, item)



  #ZIP

fruits = ['banana', 'orange', 'apple']
vegetables = ['carrot', 'potato', 'cabbage' , 'spinach']

fruits_and_veges = []

for f , v in zip(fruits, vegetables):
   fruits_and_veges.append({f , v})

print(fruits_and_veges)

