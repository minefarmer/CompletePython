'''
>>> names = ['Sandra', 'Roger', 'Carl']
>>> names       
['Sandra', 'Roger', 'Carl']
>>> type(names) 
<class 'list'>
>>> 'Carl' in names
True
>>> 'carl' in names 
False
>>> if 'Sandra' in names:
>>> print("Sandra is in the list of names!")     
Sandra is in the list of names!
>>>


'''
my_answer = "rock"
options = ["rock", "paper", "scissors"]

# if my_answer in options:
#     print("Rock is one of the possible options!")  # Rock is one of the possible options!



# my_answer = "something_else"
# options = ["rock", "paper", "scissors"]

# if my_answer in options:
#     print("Rock is one of the possible options!")  # Nothing is printed!



# my_answer = input("What is your answer? ")  # paper  answer# That option is a viable option
# options = ["rock", "paper", "scissors"]

# if my_answer in options:
#     print("That option is a viable option")  # Nothing is printed!
# else:
#     print("Wrong answer, try again")



# my_answer = input("What is your answer? ")  # Python
# options = ["rock", "paper", "scissors"]

# if my_answer in options:
#     print("That option is a viable option")
# else:
#     print("Wrong answer, try again")  # Wrong answer, try again



# key = "name"
# person = {
#     "name": "Rich",
#     "profession": "Coding Teacher"
# }

# if key in person:
#     print("Name is a valid dictionary key ")  # Name is a valid dictionary key



key = "404"
person = {
    "name": "Rich",
    "profession": "Coding Teacher"
}

if key in person:
    print("Name is a valid dictionary key ")  # Nothing happens here

