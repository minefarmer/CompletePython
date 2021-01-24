'''
Tuples are immutable  # cannot be changed

            A list that can be changed
>>> animals = ["Cat", "Dog", "Zebra", "Aardvaark"]
>>> animals
['Cat', 'Dog', 'Zebra', 'Aardvaark']
>>> animals.sort()
>>> animals
['Aardvaark', 'Cat', 'Dog', 'Zebra']
>>> 
>>> 
>>> foods = ('Pizza', 'Orange', 'Apple', 'Pasta')
>>> type(foods)
<class 'tuple'>

>>> foods
('Pizza', 'Orange', 'Apple', 'Pasta')
>>> foods.sort
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
'''

foods = ('Pizza', 'Fish', 'Tomatoes')
for food in foods:
    print("The food is", food)  # The food is Pizza
                                # The food is Fish
                                # The food is Tomatoes