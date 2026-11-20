#Determining whether the number is odd or even number
number = int(input("Please enter your number: "))
division = number % 2
if division == 1:
    print("This is an odd number")
else:
    print("This is an even number")