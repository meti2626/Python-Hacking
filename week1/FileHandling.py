
import os 
import json
# with open('c:\\Python-Hacking\\week1\\example.txt' , 'a') as f:
#     f.write('append this at the end of the file')

# os.remove('.\\week1\\example.txt')

# with open('c:\\Python-Hacking\\week1\\example.txt' , 'w') as f:
#    f.write('append this at the end of the file')

# if os.path.exists('.\\week1\\exmple.txt'):
#     os.remove('.\\week1\\exmple.txt')
# else:
#     print("The file does not exist")



#dictionary

# person_dct = {
#   "name" : "john",
#   "country" : "USA",
#   "city" : "Helsinki",
#   "skills" : ["JavaScript" , "React" ,"Python"]
# }


# person_json = '''{
# "name" : "john",
#   "country" : "USA",
#   "city" : "Helsinki",
#   "skills" : ["JavaScript" , "React" ,"Python"]
 
# }'''



# person_dct  = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print





person_dcn = {
"name" : "john",
  "country" : "USA",
  "city" : "Helsinki",
  "skills" : ["JavaScript" , "React" ,"Python"]
 
}



with open('.\\week1\\person.json' , 'w') as f:
    json.dump(person_dcn, f , indent = 4)
