class Animal:
    location = "Bihar"
    def __init__(self, name):
        self.name = name

    def speak (self):
        print("generic animal sound")
class Dog(Animal):
    def speak(self):
        super().speak() # we are you speak() function of parent class
        print(f"{self.name} is barking")
        


# a = Animal("cat")
# a.speak()

a = Dog("Jerry")
a.speak()
print(a.location)