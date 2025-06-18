
# 2 types of loop -- while loop - for loop

##while loop

# while condition :
   
# count = 0
# while count < 5 :
#   print(count)
#   count += 1
# else:
#   print(count)


# Break and continue 

# Break use it with some condition 

# count = 0
# while count < 5 :
#   print(count)
#   count += 1
#   if count == 3:
#     break


# continue - skip the current iteration and continue with the next iteration
# count = 0
# while count  < 5:
#   if count == 3:
#     count += 1
#     continue
#   print(count)
#   count += 1



#For Loop  -- use in and  and iterables 

# with list 

# numbers = [1,2,3,4,5,6]

# for num in numbers:
#   print(num + 1)


#with string 

# language = "python"

# for letter in language :
#   print(letter.upper())



# with range
# language = "python"
# for i in range(len(language)):
#     print(language[i])


#tuple

# numbers = (0,1,2,3,4)

# for num in numbers:
#   print(num)



## dictionary

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }


# for key in person:
#   print (key)
 
# for key, value in person.items():
#     print(key , ":" ,value)


numbers = [1,2,3,4,5,6,7,8,9,10]

# for num in numbers :
#    print(num)
#    if num == 5:
#       break

# for num in numbers:
#  if num ==1:
#   continue
#  print(num)  


# range funtion - range(start(0), stop, step(1))   --m if its one argument its the end


# lst = list(range(11))

# print(lst)

# st = set(range(1,11))
# print(st)


# for num in range(11):
#   print(num)



#nested loop



# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# for key in person:
#   if key == 'skills':
#     for skills in person['skills']:
#       print(skills)

# for num in range(11):
#     print(num)
# else:
#     print("Loop completed successfully")

# for num in range(6):
#   pass



# for num in range(1,8):
#   print(num*'#')


# for i in range(8):
#   for j in range(8):
#     print(' # ', end='')
#   print()



# for num in range(11):
#       mult =num*num
#       print(f"{num}*{num} = {mult}" )


lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lst:
  print(i)
  