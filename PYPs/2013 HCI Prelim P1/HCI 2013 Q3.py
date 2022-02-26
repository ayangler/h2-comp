def HighestAndAverage():
    f = open("MARKS.txt")
    data = [line.strip().split(",") for line in f]
    f.close()
    highest = data[0]
    for student in data[1:]:
        if int(student[2]) > int(highest[2]):
            highest = student
    print("This student: {}, scored the highest mark of {}.".format(highest[1], highest[2]))

    avg = 0
    for student in data:
        avg += int(student[2])
    avg /= len(data)

    print("The average score of the module is {:.2f}".format(avg))

    return int(highest[2]), float("{:.2f}".format(avg)), data


def GenerateGrades():
    high, avg, data = HighestAndAverage()
    f = open("GRADES.TXT", "w+")
    grades = []
    for student in data:
        if int(student[2]) == high:
            grade = "M"
        elif int(student[2]) < avg - 10:
            grade = "F"
        else:
            grade = "P"

        grades.append(",".join(student) + "," + str(avg) + "," + grade + "\n")

    f.writelines(grades)
    f.close()


GenerateGrades()

HighestAndAverage()
