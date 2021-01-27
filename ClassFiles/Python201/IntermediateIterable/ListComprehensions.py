# numbers = []
# for num in [1, 3, 5, 7, 9]:
#     numbers.append(num**2)
# print(numbers)  # [1, 9, 25, 49, 81]



#  The Python way
numbers = [num**2 for num in [1, 3, 5, 7, 9]]
print(numbers)  # [1, 9, 25, 49, 81]
