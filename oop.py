# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("this is first project")


# s1=student("ali",25)
# print(s1.name,s1.age)


#oop 
# class Student:

#     college="abc college"
#     print(college)

#     def __init__(self,name,age,department):
#         self.name= name
#         self.age=age
#         self.department=department
#         print("IT department students")

#     def wellcome(self):
#         print("wellcome students",self.name)
    
#     def age(self):
#         return self.age

# s1=Student("ali",25,"CS")
# print(s1.name,s1.age,s1.department)

# s2=Student("usman",24,"sw")
# print(s2.name,s2.age,s2.department)


# s1.wellcome()
# s2.wellcome()

# print(s1.age)




class Car:
    def __init__(self, make, model, year):  # Constructor to initialize object attributes
        self.make = make
        self.model = model
        self.year = year

    def accelerate(self):  # Method to simulate acceleration
        print(self.make, self.model, "is accelerating!")

my_car = Car("Honda", "Civic", 2023)
my_car.accelerate()  # Output: Honda Civic is accelerating!

    

        










        









# class Car:
#     color="black"
#     brand="bmw"

# s1=Car()
# print(s1.color)
# print(s1.brand)