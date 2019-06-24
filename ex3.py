"""""
Week #1 Exercise 3
"""""

num = int(input("Please enter a number"))
count = 0

for i in range(1, num+1):
    while count < i:
        print(f"*", end="")
        count += 1

    print()
    count = 0




