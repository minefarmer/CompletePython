items = ['One', 'Two', 'Three', 'Four','Five']

for item in items:
    if item == 'Two':
        continue  #  Completely skip 'Two'
    print(item)  # One  # Three  # Four  # Five
    
    
    
for item in items:
    if item == 'Two' or item == 'Four':
        continue  #  Completely skip 'Two'
    print(item)  # One  # Three  # five



for item in items:
    if item == "Three":
        break
    print(item)  # One  # Two



num = 0
while num <= 10:
    num = num + 1
    if num % 2 == 0:
        continue
    print(num)  # 1  # 3  # 5  # 7 # 9 # 11
    
    
    
num = 0
while num <= 20:
    num = num + 1
    if num == 7:
        break
    print(num)  # 1  # 2  # 3 # 4 # 5 # 6
