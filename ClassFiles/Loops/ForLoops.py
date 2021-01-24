'''                 For loops
A for loop is just a way to iterate through some sort of iterable and is going to allow us to take an action based on every item in a list, a tuple, asset or a string.







'''
fav_foods = ['Pizza', 'Tacos', 'Salmon']

# for food in fav_foods:  # print(food)  # Pizza    # Tacos    # Salmon
#     # print(f"My fav food is: {food}")  # My fav food is: Pizza
#                                         # My fav food is: Tacos    
#                                         # My fav food is: Salmon


#     if food == "Pizza":
#         size = input("What size pissa would you like? ")  # What size pissa would you like? medium
#         print(f"You ordered a {size} pizza")  # You ordered a medium pizza
    
    

# fav_foods = set(fav_foods)

# for food in fav_foods:
#     print(food)  # Tacos  # Pizza  # Salmon



fav_foods = tuple(fav_foods)

for food in fav_foods:
    print(food)  # Tacos  # Pizza  # Salmon



food = "Pizza!"
for letter in food:
    print(letter)  # P  # i  # z  # z  # a  # !
    
    
    
person = {
    "name": "Carl",
    "twitter": "@CarlMatson",
    "instagram": "@coding.for.everybody"
}
for value in person:
    print(value)  # name  # twitter  # instagram
    
    
    
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")  #   The key is name and the value is Carl
    # The key is twitter and the value is @CarlMatson
    # The key is instagram and the value is @coding.for.everybody
