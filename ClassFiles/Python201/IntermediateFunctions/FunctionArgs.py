# def add_numbers(*args):  #*args always comeback as a tuple
#     print(args)  # (1, 3, 5, 7, 9)
#     print(type(args))  # <class 'tuple'>

# add_numbers(1, 3, 5, 7, 9)

def add_numbers(name, *args):  #*args always comeback as a tuple
    total = 0
    for num in args:
        total = total + num
    return total
total = add_numbers('Carl', 1, 3, 5, 7, 9)
print(total)  # 25

