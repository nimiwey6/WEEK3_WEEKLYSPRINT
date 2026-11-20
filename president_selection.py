#using the students score to judge if he or she is deem fit to run for school president

print("Run for School President!!!!!!!")

user = input("Please Enter Your Name: ")
score = int(input("Please enter school result: "))
if score >= 75:
    print(f"{user}, You can run for school president!!")
else:
    print(f"{user}, You can not run for school president!!")