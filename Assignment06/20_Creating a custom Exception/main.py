class InvalidAgeError(Exception):
    pass



def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be atleast 18")
    

try:
    user_age = int(input("Enter your Age ?"))
    check_age(user_age)
    print("Access Granted!")
except InvalidAgeError as e:
    print(f"Access denied: {e}")
