# validate user input exercise .
# 1. usrename is not more then 12 characters 
# 2. username not contain space
# 3. username ust not contain digit

user_name = input("Enter your user_name:- ")

user_name.find(" ")
if len(user_name) > 12:
    print("Your user name can't be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("your user nmae can't contain spaces")
elif not user_name.isalpha():
    print("your user name can't contain numbers")
else :
    print(f"Welocome {user_name}")
