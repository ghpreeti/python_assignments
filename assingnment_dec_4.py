# oop exercise 1
# class vehicle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed=max_speed
#         self.mileage=mileage

# bmw=vehicle(300,15)        
# print("max_speed" bmw.max_speed," ", bmw.mileage)

#OOP Exercise 1: Create a Class with instance attributes

class Vehicle:    
    def __init__(self,name,max_speed,mileage):        
        self.name=name        
        self.max_speed=max_speed        
        self.mileage=mileage    
        def vehicle1(self):        
            return "hi"
a=Vehicle("shiinde",24,34)
print(a.name)
print(a.max_speed)
print(a.mileage)

#OOP Exercise 2: Create a Vehicle class without any variables and methods
class vehicle:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
 
class Vehicle: 
       def __init__(self,name,max_speed,mileage):
        self.name=name        
        self.max_speed=max_speed        
        self.mileage=mileage    
       def vehicle1(self):        
        return "hi"
class Bus(Vehicle): 
        def __init__(self):        
            Vehicle.__init__(self ,name="shinde",max_speed=24,mileage=56) 

b=Bus()
print(b.name)
print(b.max_speed)
print(b.mileage)


#Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

class Vehicle:    
    def __init__(self,name,max_speed,mileage):       
         self.name=name
         self.max_speed=max_speed        
         self.mileage=mileage    
         def vehicle1(self):        
            return "hi"
    class Bus(Vehicle):    
        def __init__(self):        
            Vehicle.__init__(self ,name="school volvo",max_speed=180,mileage=12)    
            
b=Bus()
print(b.name)
print(b.max_speed)
print(b.mileage)


# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):    
    def __init__(self):        
        Vehicle.__init__(self ,name="School volvo",max_speed=150,mileage=12)    
b=Bus()
print(b.name)
print(b.max_speed)
print(b.mileage)
print(b.seating_capacity())       


