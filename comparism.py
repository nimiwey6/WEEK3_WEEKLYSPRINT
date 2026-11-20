#Comparing of 2 number and indicating the larger one or whether they are both equal
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is the larger number")
elif num1 < num2:
    print(f"{num2} is the larger number")
else:
    print("Both numbers are equal")