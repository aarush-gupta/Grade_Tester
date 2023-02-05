average = 0
kid_grade = []
kid_name = []
grade = 0
name = 0


def name_print(kid_name):
    print(kid_name)


def name_add(kid_name):
    name = input("enter name: ")
    kid_name.append(name)
    grade = int(input("enter grade: "))
    kid_grade.append(grade)
    print(name + " name added to list. List:" + str(kid_name))


while True:
    inputter = input(" Q to quit \n V to view all Names \n G to view all grades \n E for average grade \n A to add name \n F to find if this student got above or below average \n Enter your option: ")
    if inputter == "Q":
        break
    elif inputter == "V":
        name_print(kid_name)

    elif inputter == "G":
        print(str(kid_grade))

    elif inputter == "A":
        name_add(kid_name)

    elif inputter == "F":
        average = sum(kid_grade)/len(kid_grade)
        name = input("enter name of kid you wan to find")
        position = kid_name.index(name)
        grade = kid_grade[position]
        if grade > average:
            print(name + "'s grade was better than the average:" + str(average) + ". " + name + "'s grade was:" + str(grade))
        elif grade == average:
            print(name + "'s grade was equal to the average:" + str(average) + ". " + name + "'s grade was:" + str(grade))
        else:
            print(name + "'s grade was less than the average:" + str(average) + ". " + name + "'s grade was:" + str(grade))

    elif inputter == "E":
        average = sum(kid_grade)/len(kid_grade)
        print("The average grade of the students is " + str(average))

    else:
        print("invalid choice " + inputter)
