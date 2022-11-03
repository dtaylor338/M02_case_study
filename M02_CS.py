#Drew Taylor
#M02_CS.py
#This app will test whether a student has made the dean's list or honor roll
lname=str("zz")
while lname != str("zzz"):
    lname= input("Enter your last name, to exit enter zzz: ")
    if lname == str("zzz"):
        break
    fname= input("Enter your first name: ")
    gpa= float(input("Enter your GPA: "))
    if gpa >= 3.5:
        print(fname, lname, "made the Dean's list")
    if gpa >= 3.25:
        print(fname, lname, "made the Honor Roll")