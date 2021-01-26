#  Creating the file, then writing to the file, in one operation.
# with open("writing_files.txt", 'w') as file:
#     file.write("Hello from Python 201")



# Second run of the file --- it over wrote the original file.
# with open("writing_files.txt", 'w') as file:
#     file.write("Hello from Python 201 a second time")  # Hello from Python 201 a second time


# Appending a file
with open("writing_files.txt", 'a') as file:
    file.write("\nA second line!")
    file.write("\n\tThis is tabbed!")  # Hello from Python 201 a second time
                                       # A second line!
                                       #     This is tabbed!
