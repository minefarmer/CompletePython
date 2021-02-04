'''
class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass
    
    def chase(self):
        pass

tiger = Animal()
tiger.speak()  # Raawwwrr


class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass
    
    def chase(self):
        pass

class Tiger(Animal):
    pass

tiger = Tiger()
tiger.speak()  # Raawwwrr
print(type(tiger))  # <class '__main__.Tiger'>



class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass
    
    def chase(self):
        pass

class Tiger(Animal):
    pass

tiger = Animal()
tiger.speak()  # Raawwwrr
print(type(tiger))  # <class '__main__.Tiger'>




class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass
    
    def chase(self):
        pass

class Tiger(Animal):
    def speak(self):
        print("They're GREEEEEAATTTTTTT")

tiger = Tiger()
tiger.speak()  # They're GREEEEEAATTTTTTT

'''
class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass
    
    def chase(self):
        pass

class Tiger(Animal):
    def speak(self):
        print("They're GREEEEEAATTTTTTT")

class HouseCat(Animal):

    fur_color = "Black"

    def speak(self):
        print("Meow")

tiger = Tiger()
tiger.speak()  # They're GREEEEEAATTTTTTT
cat = HouseCat()
cat.speak()  # Meow
print(cat.fur_color)  # Black

