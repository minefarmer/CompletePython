'''
Class methods are just a fancy term for a function inside of a class.



class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Carl', 'Rich', 'Sis']

    def this_is_a_method(self):
        print(self.this_list)

the_animal = Animal()
the_animal.this_is_a_method()  # ['Carl', 'Rich', 'Sis']



class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Carl', 'Rich', 'Sis']

    def this_is_a_method(self):
        print(self.this_list)

    @property
    def get_sis(self):
        return self.this_list[2]

the_animal = Animal()
the_animal.this_is_a_method()  # ['Carl', 'Rich', 'Sis']
sis = the_animal.get_sis
print("The cutest gato of all time is", sis)  # The cutest gato of all time is Sis


'''
class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Carl', 'Rich', 'Sis']

    def  add_name(self, name):
        self.this_list.append(name)
        return self.this_list

    def this_is_a_method(self):
        print(self.this_list)

    @property
    def get_sis(self):
        return self.this_list[2]

the_animal = Animal()
the_animal.add_name("Roger")
print(the_animal.this_list)  # ['Carl', 'Rich', 'Sis', {'Roger'}]





