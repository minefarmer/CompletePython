# class Animal:
#     fur_color = "Orange"

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self):
#         pass

# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")

# cat = HouseCat()
# cat.eat()  # I am eating yum yum



# class Animal:
#     fur_color = "Orange"

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self):
#         pass

# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")
    
#     def eat(self):
#         print("I am eating salmon")

# cat = HouseCat()
# cat.eat()  # I am eating salmon


# class Animal:
#     fur_color = "Orange"

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self):
#         pass

# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")
    
#     def eat(self):
#         super().eat()
#         print("I am eating salmon")

# cat = HouseCat()
# cat.eat()  # I am eating yum yum
#             # I am eating salmon



# class Animal:
#     fur_color = "Orange"

#     def speak(self):
#          raise NotImplementedError

#     def eat(self):
#         print("I am eating yum yum")
    
#     def chase(self, animal="Gazelle"):
#         print("I am chasing", animal)

# class HouseCat(Animal):
#     def speak(self):
#         print("Meow")
    
#     def eat(self):
#         super().eat()
#         print("I am eating salmon")

# cat = HouseCat()
# cat.chase()  # I am chasing Gazelle



# class Animal:
#     fur_color = "Orange"

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

# cat = HouseCat()
# cat.chase("Mouse")   # I am chasing a Mouse



class Animal:
    fur_color = "Orange"

    def speak(self):
         raise NotImplementedError

    def eat(self):
        print("I am eating yum yum")
    
    def chase(self, animal="Gazelle"):
        print("I am chasing a", animal)

class HouseCat(Animal):
    def speak(self):
        print("Meow")
    
    def eat(self):
        super().eat()
        print("I am eating salmon")
    
    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat()
cat.chase("mouse")   # I am chasing a mouse
                    # mouse was caught
