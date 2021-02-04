'''
##### when it comes to automatically assigning properties, I can do that with a dundar method.  i.e. __init__



# A property as a dictionary inside a class
class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }


the_animal = Animal()
print(the_animal.this_is_a_property)  # {'key_1': 'Value 1'}


class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }

the_animal = Animal()
print(the_animal.this_is_a_property['key_1'])  # Value 1


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# A property as a list inside a class
class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Carl', 'Rich', 'Sis']

the_animal = Animal()
print(the_animal.this_list)  # ['Carl', 'Rich', 'Sis']



class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Carl', 'Rich', 'Sis']

the_animal = Animal()
print(the_animal.this_list[2])  # Sis



### accessing this property directly, by it's class directly ^^^^^^^^^^^^^^^^^^

class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Carl', 'Rich', 'Sis']

print(Animal.this_list)  # ['Carl', 'Rich', 'Sis']




'''


