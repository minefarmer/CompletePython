# class Animal:
#     fur_color = "Orange"

#     def __init__(self, fur_color):
#         pass

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self, animal="Gazelle"):
#         print("I am chasing a", animal)

# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")
    
#     def eat(self):
#         super().eat()
#         print("I am eating salmon")
    
#     def chase(self, animal):
#         super().chase(animal)
#         print(animal, "was caught")

# cat = HouseCat("Grey")
# cat.chase("mouse")  # I am chasing a mouse
#                     # mouse was caught



# class Animal:
#     fur_color = "Orange"

#     def __init__(self, fur_color):
#         print(f"Fur color is {fur_color}")  # Fur color is Grey
#         pass

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self, animal="Gazelle"):
#         print("I am chasing a", animal)

# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")
    
#     def eat(self):
#         super().eat()
#         print("I am eating salmon")
    
#     def chase(self, animal):
#         super().chase(animal)
#         print(animal, "was caught")

# cat = HouseCat("Grey")
# cat.chase("mouse")  # I am chasing a mouse
#                     # mouse was caught



# class Animal:

#     def __init__(self, fur_color):
#         self.fur_color = fur_color

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self, animal="Gazelle"):
#         print("I am chasing a", animal)
    
#     def get_fur_color(self):
#         print("Getting fur color: ", self.fur_color)  # Getting fur color:  Orange


# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")
    
#     def eat(self):
#         super().eat()
#         print("I am eating salmon")
    
#     def chase(self, animal):
#         super().chase(animal)
#         print(animal, "was caught")

# cat = HouseCat("Orange")
# cat.get_fur_color()











class Animal:

    animal_type = "Unknown"

    def __init__(self, fur_color):
        self.fur_color = fur_color

    def speak(self):
         raise NotImplementedError

    def eat(self):
        print("I am eating yum yum")
    
    def chase(self, animal="Gazelle"):
        print("I am chasing a", animal)
    
    def get_fur_color(self):
        print("Getting fur color: ", self.fur_color)  # Getting fur color:  Orange


class HouseCat(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color  was saved to the class Object")  # Fur color  was saved to the class Object
        self.animal_type = "House cat"
        print(self.animal_type)  # House cat


    def speak(self):
        print("Meow")
    
    def eat(self):
        super().eat()
        print("I am eating salmon")
    
    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat("Orange")
cat.get_fur_color()
