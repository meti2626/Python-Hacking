
#if condition
# a = 1

# if a > 0:
#   print("a  is positive")
# elif a < 0:
#   print ("a is -ve")
# else:
#   print("a is 0")

# #short hand  

# print("a id ve") if a < 0 else print("a is positive")

# #nested conditions 

# a = 2

# if a > 0:
#   if a%2 == 0:
#      print ("a is even")
#   else :
#     print("a is odd")
# elif  a < 0:
#   print("a is -ve")
# else:
#   print("a is 0")




# if condition or condition
    #code 




# user = 'james'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#     print("access granted")
# else:
#     print("access denied")


# print("Enter your age : ")
# age = int(input())

# if age>= 18:
#    print("you can drive")
# else:
#    print("you cannot drive")

age1 = 20
print("Enter your age2 : ")
age2 = int(input())

if age1 > age2:
   diff = age1 - age2
   if diff == 1:
      print ("You are younger by 1 year")
   elif diff > 1:
      print(f"you are younger by {diff} years")
   else :
      print("you are twinning")

elif age2 > age1:
   diff = age2 - age1
   if diff == 1:
      print ("You are older by 1 year")
   elif diff > 1:
      print(f"you are older by {diff} years")
   else :
      print("you are twinning")


else:
  print("you are the same age")
