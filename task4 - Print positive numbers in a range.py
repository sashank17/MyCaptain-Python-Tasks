list1 = [12,-7,5,64,-14]
print("Input: list1 =", list1)
print("Output:", end=' ')
for i in list1:
    if i>=0:
        print(i, end=',')
print()
list2 = [12,14,-95,3]
print("Input: list2 =", list2)
print("Output:", end=' [')
for i in list2:
    if i>=0:
        print(i, end=',')
print("]")
