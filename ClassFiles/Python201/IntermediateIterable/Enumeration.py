# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
# for animal in enumerate(animals):   # creates a list of Tuples
#     print(animal)  # (0, 'Gully')
#                     # (1, 'Rhubarb')
#                     # (2, 'Zephyr')
#                     # (3, 'Henry')



# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
# for index, animal in enumerate(animals):
#     print(animal)  # Gully
#                     # Rhubarb
#                     # Zephyr
#                     # Henry

# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
# for index, animal in enumerate(animals):
#     print(index, animal)  # 0 Gully
#                         # 1 Rhubarb
#                         # 2 Zephyr
#                         # 3 Henry



# animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
# for index, animal in enumerate(animals):
#     if index % 2 == 0:
#         continue
#     print(index, animal)  # 1 Rhubarb
#                         #   3 Henry



animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]
for index, animal in enumerate(animals):
    # if index % 2 == 0:
    #     continue
    print(f"{index}.\t {animal}")   # 0.       Gully
                                    # 1.       Rhubarb
                                    # 2.       Zephyr
                                    # 3.       Henry
