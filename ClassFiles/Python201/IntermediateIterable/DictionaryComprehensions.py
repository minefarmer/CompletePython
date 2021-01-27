# names = [("name", "Rich"), ("occupation", "retired")]
# d = {}
# for key, value in names:
#     d[key] = value  # {'name': 'Rich', 'occupation': 'retired'}  # source of (d on line 5.)
# print(d)  # {'name': 'Rich', 'occupation': 'retired'}
# print(type(d))  # <class 'dict'>



# Python way
names = [("name", "Rich"), ("occupation", "retired")]

# d = {key: value for key, value in names}  # only for this lesson
# print(d)  # {'name': 'Rich', 'occupation': 'retired'}

d = dict(names)
print(d)  # {'name': 'Rich', 'occupation': 'retired'}
