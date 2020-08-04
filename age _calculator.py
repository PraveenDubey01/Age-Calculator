import datetime
birthyear = int(input("ENTER YOUR BIRTH YEAR : "))
age = datetime.datetime.now().year-birthyear
print("YOUR AGE IS", age , "YEARS OLD")