def most_frequent(string):
    string = string.lower()
    letters1 = {}
    for letter in string:
        c = string.count(letter)
        letters1[letter] = c
    letters = sorted(letters1.items(), key=lambda x: x[1], reverse=True)
    for i in letters:
        print(i[0], "=", i[1])


str1 = input("Please enter a string: ")
most_frequent(str1)
