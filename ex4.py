"""""
Week #1 Exercise 4
"""""

num = int(input("Please enter a number"))
spaces = num - 1
count = 0
j = 0
num_of_asterisk = 1

for i in range(1, num+1):

    while j < spaces:
        print(f" ", end="")
        j += 1
    spaces -= 1
    j = 0

    while count < num_of_asterisk:
        print(f"*", end="")
        count += 1
    num_of_asterisk += 2
    print()
    count = 0
