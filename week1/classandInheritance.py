#classes and Object 


#syntax for class

# class Person:
#   pass
# print(Person)

# p = Person()
# print(p)


class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
#       def add__skil(self , skill):
#           self.skills.append(skill)

# p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
# print(p.person_info())

# p.add__skil('JavaScript')
# p.add__skil('React')
# p.add__skil('Node')
# print(p.skills)


##Inheritance 


class Student(Person):
      pass

s1 = Student('John', 'Doe', 20, 'USA', 'New York')
s2 = Student('Jane', 'Doe', 22, 'USA', 'Los Angeles')

print(s1.person_info())
print(s2.person_info()) 





