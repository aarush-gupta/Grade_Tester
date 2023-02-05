# Variables
kid1 = 0
kid2 = 0
kid3 = 0
kid4 = 0
kid5 = 0
kid6 = 0
kid7 = 0
kid8 = 0
kid9 = 0
kid10 = 0
kids_grade_list = []
kids_list = []
# Functions


def kid_name():
    print("Enter the name for 10 kids")
    kid1 = input("Name for Kid 1: ")
    kid2 = input("Name for Kid 2: ")
    kid3 = input("Name for Kid 3: ")
    kid4 = input("Name for Kid 4: ")
    kid5 = input("Name for Kid 5: ")
    kid6 = input("Name for Kid 6: ")
    kid7 = input("Name for Kid 7: ")
    kid8 = input("Name for Kid 8: ")
    kid9 = input("Name for Kid 9: ")
    kid10 = input("Name for Kid 10: ")
    kids_list = [kid1, kid2, kid3, kid4, kid5, kid6, kid7, kid8, kid9, kid10]


def kid_grade():
    print("Enter the name for the10 kids grades")
    kid1 = int(input("Grade for Kid 1: "))
    kid2 = int(input("Grade for Kid 2: "))
    kid3 = int(input("Grade for Kid 3: "))
    kid4 = int(input("Grade for Kid 4: "))
    kid5 = int(input("Grade for Kid 5: "))
    kid6 = int(input("Grade for Kid 6: "))
    kid7 = int(input("Grade for Kid 7: "))
    kid8 = int(input("Grade for Kid 8: "))
    kid9 = int(input("Grade for Kid 9:  "))
    kid10 = int(input("Grade for Kid 10: "))
    kids_grade_list = [kid1, kid2, kid3, kid4, kid5, kid6, kid7, kid8, kid9, kid10]


def kid_average(z):
    average = kids_grade_list.mean()
    print("The average grade of the students is " + str(average))


def add_name():
    pass


def view_name():
    pass


kid_name()
kid_grade()


# running stuff
while True:
    thing_to_do = input("Do you want to add a name(add), view names and grades(view) or find the average grade(average)? :")
    if thing_to_do == "average":
        kid_average(kids_grade_list)
    elif thing_to_do == "add":
        add_name()
    elif thing_to_do == "view":
        view_name()
