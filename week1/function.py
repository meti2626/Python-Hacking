
# def generate_full_name ():
#   first_name = 'Asabe'
#   last_name = 'Bes'
#   space = ' '
#   full_name = first_name + space + last_name
#   print (full_name)

# generate_full_name()

# def add_two_numbers():
#   num1 = 2
#   num2 = 3 
#   total = num1 + num2
#   return total

# print(add_two_numbers())


# def greetings (name):

#   greeting = name + ' ' + 'welcome to the python course'
#   return greeting

# print(greetings('dave'))



# def sum(num1 , num2 ):
#   sum = num1 + num2

#   return sum 

# print("sum =",sum(1,3))




# def greetings (name = 'Peter'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())


# 
# def sum (*nums):
#    total = 0
#    for num in nums:
#       total += num
#    return total
   
# print(sum(1,2,3,4,5,6,7))



def square_number(n):
     return n*n
def do_st(f,x):
     return f(x)
print(do_st(square_number, 5))  # Output: 25

def sn(n):
     return n*n
def ds(f , x ):
      return f(x)
print (ds(sn , 5))