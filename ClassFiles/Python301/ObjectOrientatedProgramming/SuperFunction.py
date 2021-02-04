'''




'''




class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("I am eating yum yum yum")
    
    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print("Meeeeooowwww")

cat = HouseCat()
cat.speak() 

