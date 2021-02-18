# num = input("Enter a number: ")  # 10
# try:
#     num = int(num)
# except  Exception:
#     num = "unknown"

# print(num)  # 10



# num = input("Enter a number: ")  # Python
# try:
#     num = int(num)
# except  Exception:
#     num = "unknown"

# print(num)  # Unknown



# num = input("Enter a number: ")
# try:
#     num = int(num)
# except Exception as e:
#     print("Exception was caught")  # Exception was caught
#     print(type(e))  # <class 'ValueError'>
#     num = "unknown"

# print(num)  # Unknown



# num = input("Enter a number: ")
# try:
#     num = int(num)
# except ValueError:
#     print(num, "was not a valid number")  # Python was not a valid number
# except Exception as e:
#     print("Exception was caught")  # Nothing printed
#     print(type(e))  # Nothing printed
#     num = "unknown"

# print(num)  # Python



# num = input("Enter a number: ")  # 10
# num2 = input("Enter a second number: ")  # 100
# try:
#     num = int(num)
#     num2 = int(num2)
#     total = num / num2
# except ValueError:
#     print(num, "Num or num2 was not a valid number")
# except Exception as e:
#     print("Exception was caught")  # Nothing printed
#     print(type(e))  # Nothing printed
#     num = "unknown"



# num = input("Enter a number: ")  # 10
# num2 = input("Enter a second number: ")  # 0
# try:
#     num = int(num)
#     num2 = int(num2)
#     total = num / num2
# except ValueError:
#     print(num, "Num or num2 was not a valid number")
# except Exception as e:
#     print("Exception was caught")  # Exception was caught
#     print(type(e))  # <class 'ZeroDivisionError'>
#     num = "unknown"



num = input("Enter a number: ")  # 10
num2 = input("Enter a second number: ")  # 0
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:
    print(num, "Num or num2 was not a valid number")
except ZeroDivisionError:
    print("Numbers could not be divided")  # Numbers could not be divided
except Exception as e:
    print("Exception was caught")  
    print(type(e))  
