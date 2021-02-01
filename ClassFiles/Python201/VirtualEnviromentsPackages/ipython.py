'''
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "Python 201"
>>> name,               
('Python 201',)
>>> name.
name.capitalize(    name.format_map(    name.isnumeric(     name.maketrans(     name.split(
name.casefold(      name.index(         name.isprintable(   name.partition(     name.splitlines(
name.center(        name.isalnum(       name.isspace(       name.replace(       name.startswith(
name.count(         name.isalpha(       name.istitle(       name.rfind(         name.strip(
name.encode(        name.isascii(       name.isupper(       name.rindex(        name.swapcase(
name.endswith(      name.isdecimal(     name.join(          name.rjust(         name.title(
name.expandtabs(    name.isdigit(       name.ljust(         name.rpartition(    name.translate(
name.find(          name.isidentifier(  name.lower(         name.rsplit(        name.upper(
name.format(        name.islower(       name.lstrip(        name.rstrip(        name.zfill(

>>> name.lower()
'python 201'
>>> 
>>> name.endswith("201")
True
>>> words = name.split(" ")
>>> words
['Python', '201']  # words is now a list
>>> 
>>> words.
words.append(   words.copy(     words.extend(   words.insert(   words.remove(   words.sort(     
words.clear(    words.count(    words.index(    words.pop(      words.reverse(  
>>> words.reverse()
>>> words
['201', 'Python']
>>> 
>>> course = ' '.join(words)
>>> course
'201 Python'

>>> course = ' '.join(words)
>>> course
'201 Python'
>>> words.pop()
'Python'
>>> words.pop()
'201'
>>> words
[]
>>> 


In [1]: name = "Kalob Taulin"                                                   

In [2]: name.zfill("1")                                                         
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-9e617e84d694> in <module>
----> 1 name.zfill("1")

TypeError: 'str' object cannot be interpreted as an integer


In [5]: name.zfill("test")                                                      
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-02cd806b9b5a> in <module>
----> 1 name.zfill("test")

TypeError: 'str' object cannot be interpreted as an integer



'''

