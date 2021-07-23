
value = 1234  # GLOBAL name

def spam():
    value = "wombat"
    hero = "Thor"  # LOCAL name
    print("in spam(): hero is", hero)
    print("in spam(): value is", value)

spam()
# print("in main: hero is", hero)
print("in main: value is", 1234)

class Dog:
    def bark(self):
        print("Woof woof")

    @classmethod
    def spam(cls):
        print("Hello")



d = Dog()
d.bark()   # Dog.bark(d)
d.spam()  # class method called from instance
Dog.spam()  # class method called from class

# Dog.bark(d)  # d.bark()





