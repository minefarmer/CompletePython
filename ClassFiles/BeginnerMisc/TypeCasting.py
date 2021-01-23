'''                 Type casting your data types
Changing one data type to another data type.


'''
age = input("What is your age? ")
data_type = type(age)
print(data_type)  # <class 'str'>
age = int(age)
data_type = type(age)
print(data_type)  # <class 'int'>


print("My age in dog years is", (age * 7))  # My age in dog years is 574



grocery_list = ['Apples', 'Oranges', 'Bananas', 'Apples']
grocery_list = set(grocery_list)
print(grocery_list)  # {'Bananas', 'Oranges', 'Apples'}
print(type(grocery_list))  # <class 'set'>



grocery_list = ['Apples', 'Oranges', 'Bananas', 'Apples']
grocery_list = tuple(grocery_list)
print(grocery_list)  # ('Apples', 'Oranges', 'Bananas', 'Apples')
print(type(grocery_list))  # <class 'tuple'>
