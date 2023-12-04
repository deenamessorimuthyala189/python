class Person:
    count = 0 #This is a class varible
    def __init__(self,name,age,collegename):
        self.name = name
        # this is an instance variable
        self.age = age
        self.collegename = collegename
        Person.count += 1
#acessing the class variable using the name of the class
person1 =Person("Beauty",21,"AWEC")
person2 = Person("Deena Messori",20,"AWEC")
print(Person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)