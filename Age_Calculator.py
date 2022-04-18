def age_calculator(y,m,d):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age)
y=int(input("Enter Year Of Birth:-"))
m=int(input("Enter Month Of Birth:-"))
d=int(input("Enter Date Of Birth:-"))
age_calculator(y,m,d)