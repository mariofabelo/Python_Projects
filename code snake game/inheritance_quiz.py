class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True
    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")


#
# class Labrador():
#     def__init__():
#         super().__init__()
#         self.temperament = "outgoing"

doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")

