'''                 Indexing and slicing lists
lst = [1, 2, 3, 4, 5]
       0  1  2  3  4 

'''
lst = ['one', 'two', 'three', 'four', 'five']
print(lst[0])  # one
print(lst[2])  # three
print(lst[0:3])  # ['one', 'two', 'three']
print(lst[2::])  # ['three', 'four', 'five']
print(lst[-1])  # five
print(lst[-5])  # one
print(lst[-2::])  # ['four', 'five']

course = "Python 101"
print(course[5])  # n


# A non-subscriptable  error
# b = True
# print(b[0])  # Traceback (most recent call last):
#             # File "/home/rich/Desktop/CarlsHub/CompletePython/ClassFiles/BeginnerMisc/IndexingSlicing.py", line 11, in <module>
#             #     print(b[0])
#             # TypeError: 'bool' object is not subscriptable
