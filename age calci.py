n=int(input("Select 1 to see when you be 100 year old \nSelect 2 to find your age in specific year: "))
age = int(input("Enter your AGE or year of birth(DOB): "))
if n == 1:
    # detecting if input is current age
    if age <= 150:
        current_year = int(input("enter the current year you are in: "))
        dob = current_year - age
        dob= dob + 100
        print("You will be 100 yeares old in ", dob)
    # detecting if input is in year(DOB)
    if age>150:
        age = age + 100
        print("you will be 100 years old in ", age)
        if age<1915:
            print("You seem to be oldst person alive")
            print("You are more than 100 years old.")
    # if not born yet or false input
    elif dob < current_year:
        # age == 0:
        print("you are not born yet")
        print("Enter a current input ")
elif n ==2:
    Syear = int (input("Enter the specific year in which you want to check your age: "))
    # if age 
    if age <= 150:
        current_year = int(input("enter the current year you are in: "))
        ans = Syear - current_year
        if ans <0:
            print("You are not born yet \nEnter correct input")
        print("Your age in ", Syear ,"will be ", ans)
    # if DOB
    if age>150:
        ans= Syear - age
        if ans <0:
            print("You are not born yet \nEnter correct input")
        elif age<1915:
            print("YOU seem to be oldst person alive")
            print("You are more than 100 years old.")
        print("Your age in ", Syear ,"will be ", ans)
    