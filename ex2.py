"""""
Week #1 Exercise 2 - write a program that gets 3 digits number and checks if one of the digits is a sum of the 2 others
"""""

number = int(input("Please enter a 3 digits no."))

dig_1 = number % 10
dig_2 = number % 100 // 10
dig_3 = number // 100

print(f"dig1 = {dig_1}, dig2 = {dig_2}, dig3 = {dig_3}")

if dig_1 + dig_2 == dig_3 or dig_2 + dig_3 == dig_1 or dig_1 + dig_3 == dig_2:
    print("Yes")
else:
    print("No")
