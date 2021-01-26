'''
looking at scope and how it affects functions inside of functions.

'''
# def thing1():
#     print("Welcome to thing 1")
#     def thing2():
#         print("Welcome to thing2")
#     thing2()  # This is a DECORATOR

# thing1()


#  Do not use
# def thing1(name):
#     print("Welcome to thing 1", name)
    
#     def thing2(name):
#         print("Welcome to thing 2", name)
#     thing2(name)  # This is a DECORATOR

# thing1("Carl")  # Welcome to thing 1 Carl
#                 # Welcome to thing 2 Carl



# def thing1(name):
#     print("Welcome to thing 1", name)
    
#     def thing2():  # When it didn't find anything here, it moved up three lines to thing1(name)
#         print("Welcome to thing 2", name)
#     thing2()  # This is a DECORATOR

# thing1("Carl")  # Welcome to thing 1 Carl
#                 # Welcome to thing 2 Carl



def thing1(name):
    print("Welcome to thing 1", name)
    
    def thing2():  # When it didn't find anything here, it moved up three lines to thing1(name)
        print("Welcome to thing 2", name)
    thing2()  # This is a DECORATOR

thing1("Carl")  # Welcome to thing 1 Carl
                # Welcome to thing 2 Carl
print(name)  # Traceback (most recent call last):
            # File "FunctionsInsideFunctions.py", line 48, in <module>
            #     print(name)
            # NameError: name 'name' is not defined

