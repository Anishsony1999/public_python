
# 1. Class
# 2. Object



# enginer - plan -> 3bhk
# build  home

# plan( blue print ) -> 30 home
# class ( blue print ) -> Object


# class ClassName:
class Home:
    
    def __init__(self,name,color,fan,light):
        self.name= name
        self.light = light
        self.color = color
        self.fan = fan

    def lights_on(self):
        print(f"{self.name} {self.light} light will be on")

    def hey_siri_fan_on(self):
        print(f"{self.name} {self.fan} fan Will on")

# string home1 = new String() - .net
# obj = Class()

gopika_home = Home("gopika illam","White","Usha","White") 
anish_home = Home("Sony Home","Black","Orion","Warm")

anish_home.hey_siri_fan_on()
anish_home.lights_on()
gopika_home.lights_on()
gopika_home.hey_siri_fan_on()


print(anish_home.color)

class Parent:

    def __init__(self):
        self.name = "Gopika"
    
    def add(self,x,y):
        return x+y 
    
    def mult(self,x,y):
        return x*y
    
class Child(Parent):
    pass

child = Child()

ans = child.add(2,3)
print(ans)
print(child.name)

class Bank:

    def __init__(self):
        self.name = "gopike"
        self.__balance = 35000
        self.add = "TVC"
    
    def set_balace(self,balance):
        self.__balance = balance
        print(f"Blance will added {self.__balance}")

    def get_balace(self):
        print(f"Your Balance is : {self.__balance}")

    def __adding():
        print("Adding Function")
    
    __adding() # private function will use in side the class only

gopika = Bank() # name , pass , balance
anish = Bank()
anu = Bank()

# console input , name ,pass , find  by name and pass -> welcom anish 
# 1, ceadit 
# 2, debit 

gopika.set_balace(300)
# gopika.__balance = 300
# print(gopika.balance)
gopika.get_balace()


from abc import ABC, abstractclassmethod
class Animal(ABC): # Abstract Base Class

    @abstractclassmethod 
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Whow whow")


