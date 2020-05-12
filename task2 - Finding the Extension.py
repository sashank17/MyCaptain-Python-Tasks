ext = input("Input the Filename: ")
for i in ext:
    if (i == '.'):
        print("The extension of the file is:", ext[ext.index(i):])
        break
