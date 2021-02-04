'''
class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        pass
    
    def chase(self):
        pass

class HouseCat(Animal):
    pass

cat = HouseCat()
cat.speak()  # Traceback (most recent call last):
            # File "/home/rich/Desktop/CarlsHub/CompletePython/ClassFiles/Python301/ObjectOrientatedProgramming/ClassInterfaces.py", line 17, in <module>
            #     cat.speak()  # Meow
            # File "/home/rich/Desktop/CarlsHub/CompletePython/ClassFiles/Python301/ObjectOrientatedProgramming/ClassInterfaces.py", line 5, in speak
            #     raise NotImplementedError
            # NotImplementedError



'''



class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        pass
    
    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print("Meeeeooowwww")

cat = HouseCat()
cat.speak()  # Meeeeooowwww
