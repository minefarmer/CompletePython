# try:
#     total = 1/0
#     # this will not execute
# except Exception:
#     total = 0

# print(total)  # 0


# try:
#     total = 1/0
#     print("This will not show up.")
# except Exception:
#     print("Exception was caught")  # Exception was caught
#     total = 0

# print(total)  # 0


# num = input("What is a number? ")  # What is a number? 10
# num = int(num)
# print(num)  # 10


# num = input("What is a number? ")  # What is a number? Python 301
# num = int(num)
# print(num)  # Traceback (most recent call last):
#             # File "c:\Users\pgold\CarlsHub\CompletePython\ClassFiles\Python301\ObjectOrientatedProgramming\ErrorCatching\ErrorsExceptions.py", line 26, in <module>
#             #     num = int(num)
#             # ValueError: invalid literal for int() with base 10: 'Python 301'


num = input("What is a number? ")  # What is a number? Python 301
try:
    num = int(num)
except  Exception:
    num = Unknown
print(num)
