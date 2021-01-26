# with open("ReadMe.txt",'r') as file:
#     print(file.read())  # Hello from Python 201


# #  Running after adding the second line to the .txt file
# with open("ReadMe.txt",'r') as file:
#     print(file.read())  # Hello from Python 201
#                         # This is a new line


# #  Running after adding the second line to the .txt file
# with open("ReadMe.txt",'r') as file:
#     pass

# print(file.read())  # Traceback (most recent call last):
#                     # File "ReadingFiles.py", line 15, in <module>
#                     #     print(file.read())  
#                     # ValueError: I/O operation on closed file.


#  Assigning the content to a variable and then reading the file
with open("ReadMe.txt",'r') as file:
    content = file.read()
    # python has closed the file
print("The content is", content)   #  The content is Hello from Python 201
                                    # This is a new line  
