''' function somename() {
    
}

def somename():
    pass 

somename() # runs the function

'''
def somename():
    print("Hello World!")

somename()  # Hello World!



name = "Rich"
def somename():
    print(f"Hello {name}")  # Hello Rich

somename()



def somename(name):
    print(f"Hello {name}")  # Hello Jess

somename('Jess')



def somename(name, food):
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Jess. Let's eat some Tacos.

somename('Jess', 'Tacos')



def somename(name, food="Pizza"):  # food is a keyword argument
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Jess. Let's eat some Pizza.

somename('Jess')



#  Overwriting the (second(default value))
def somename(name, food="Pizza"):
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Jess. Let's eat some Oranges.

somename('Jess', 'Oranges')



#  Overwriting the (second(default value))  ###  somename('Jess', food='Oranges')
def somename(name, food="Pizza"):
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Jess. Let's eat some Oranges.

somename('Jess', food='Oranges')



def somename(name, food="Pizza"):
    if name.lower() == "jess":
        print("Welcome Jess")  # Welcome Jess
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Jess. Let's eat some Oranges.

somename('Jess', food='Oranges')



def somename(name, food="Pizza"):
    if name.lower() == "jess":
        print("Welcome Jess")  # Welcome Jess
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Beth. Let's eat some Oranges.

somename('Beth', food='Oranges')



def somename(name=None, food="Pizza"):
    print(f"Hello {name}. Let's eat some {food}.")  # Hello None. Let's eat some Oranges.

somename()
   


def somename(name=None, food="Pizza"):
    if name is None:
        name = "Evan"
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Evan. Let's eat some Oranges.

somename()
   

##########################################################################
# def somename(name=None, food="Pizza"):  # This is not working
#     if name is None:
#         name = "Evan"
    
#     person_type = "Cat"
#     if name == "Zypher":
#         person_type = "human"
        
#     print(person_type)  # Cat

# somename()

#########################################################################

def somename(name=None, food="Pizza"):
    if name is None:
        name = "Evan"
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Evan. Let's eat some Oranges.

some_var = somename()

print("The variable is ", some_var)  # The variable is  None



def somename(name=None, food="Pizza"):
    if name is None:
        name = "Evan"
    print(f"Hello {name}. Let's eat some {food}.")  # Hello Evan. Let's eat some Oranges.

some_var = somename()

print("The variable is ", some_var)  # The variable is  None



def somefunction():
    return "a value"

thing = somefunction()
print(thing)  # a value



def exp(num1, num2):
    total = num1 ** num2
    return total

big_number = exp(33, 6)
big_number2 = exp(12, 12)
print(big_number)  # 1291467969
print(big_number2)  # 8916100448256
    