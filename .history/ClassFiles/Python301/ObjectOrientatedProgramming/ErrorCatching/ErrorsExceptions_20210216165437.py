# try:
#     total = 1/0
#     pr this will not execute
# except Exception:
#     total = 0

# print(total)  # 0


try:
    total = 1/0
    # this will not execute
except Exception:
    total = 0

print(total)  # 0
