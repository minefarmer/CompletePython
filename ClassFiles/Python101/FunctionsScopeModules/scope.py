def myfunc(name):  # Best practice is to put the name here
    # name = "Sis"
    return name

myfunc()
print(myfunc())  # Sandra
print(name)  # Sandra
'''


def myfunc():
    name = "Matson"
    return name

myfunc()
print(name)  # Traceback (most recent call last):
            # File "/home/rich/Desktop/CarlsHub/CompletePython/ClassFiles/FunctionsScopeModules/scope.py", line 6, in <module>
            #     print(name)  # Traceback (most recent call last):
            # NameError: name 'name' is not defined



# Scoping
name = "Sandra"
def myfunc():
    return name  # The function first looks here, = it goes out side that function, etc., untill it gets to the global scope to look for a name

myfunc()
print(myfunc())  # Sandra



name = "Sandra"
def myfunc():
    name = "Sis"
    return name

myfunc()
print(myfunc())  # Sis
print(name)  # Sandra



name = "Sandra"
def myfunc():
    # name = "Sis"
    return name

myfunc()
print(myfunc())  # Sandra
print(name)  # Sandra



def myfunc():
    # name = "Sis"
    return name

myfunc()
print(myfunc())
print(name) #Traceback (most recent call last):
            # File "/home/rich/Desktop/CarlsHub/CompletePython/ClassFiles/FunctionsScopeModules/scope.py", line 49, in <module>
            #     myfunc()
            # File "/home/rich/Desktop/CarlsHub/CompletePython/ClassFiles/FunctionsScopeModules/scope.py", line 47, in myfunc
            #     return name
            # NameError: name 'name' is not defined
'''
