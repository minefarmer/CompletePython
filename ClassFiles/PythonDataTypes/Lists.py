lst = ["string", 1, 3.14, ["A new item"], "Richard"]
print(lst)  # ['string', 1, 3.14, ['A new item'], 'Richard']

# for item in lst:
#     print("The item is:", item)  # The item is: string
#                                 # The item is: 1
#                                 # The item is: 3.14
#                                 # The item is: ['A new item']
#                                 # The item is: Richard


>>> names = ["Richard", "Matson"]
>>> names
['Richard', 'Matson']
>>> 
>>> names.append("Jon")
>>> names
['Richard', 'Matson', 'Jon']
>>> 
>>> names.remove('Matson')
>>> names
['Richard', 'Jon']
>>> Jon = names.pop()
>>> names
['Richard']