class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("sit")

    def roll_over(self):
        print("roll over")

my_dog = Dog("Rex", "Superdog")



print(my_dog)
print(my_dog.name)
print(my_dog.breed)
