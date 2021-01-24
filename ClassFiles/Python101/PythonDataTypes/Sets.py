'''                 Set data type

lst = [varname, varname1, varname2]
dictionary = {
    "key": "value",
}
'''
set = {"Item1", "Item2", "Item3"}
print(set)  # {'Item1', 'Item2', 'Item3'}  # Sets do not care about the order
            # {'Item2', 'Item3', 'Item1'}  # Sets do not care about the order

s = {"Item1", "Item2", "Item2", "Item3"}
print(s)  # {'Item3', 'Item2', 'Item1'}  ## Second item2 considered a duplicate

s.add("item 4")
print(s)  #{'Item2', 'Item1', 'item 4', 'Item3'}

s.remove("item 4")
print(s)  # {'Item1', 'Item2', 'Item3'}

