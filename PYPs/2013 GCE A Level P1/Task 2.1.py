# Task 2.1

def search(Array1, Array2, SearchItem, repeat=False):
    found = []

    for i in range(1, len(Array1)):
        if SearchItem == Array1[i]:
            found.append(Array2[i])
            if not repeat:  # search by unique ID
                return found
    return found  # sesacrh by surname


def printMenu():
    print("=" * 25)
    print("1. Search by surname")
    print("2. Search by employee ID")
    print("3. Exit")
    print("=" * 25)


def main():
    # Initialise data
    EmployeeCode = [""] * 33
    Surname = [""] * 33
    EmployeeCode[1] = "L001"
    Surname[1] = "Pollard"
    EmployeeCode[2] = "L002"
    Surname[2] = "Wills"
    EmployeeCode[3] = "L007"
    Surname[3] = "Singh"
    EmployeeCode[4] = "L008"
    Surname[4] = "Yallop"
    EmployeeCode[5] = "L009"
    Surname[5] = "Adams"
    EmployeeCode[6] = "L013"
    Surname[6] = "Davies"
    EmployeeCode[7] = "L014"
    Surname[7] = "Patel"
    EmployeeCode[8] = "L021"
    Surname[8] = "Kelly"
    EmployeeCode[9] = "S001"
    Surname[9] = "Ong"
    EmployeeCode[10] = "S002"
    Surname[10] = "Goh"
    EmployeeCode[11] = "S003"
    Surname[11] = "Ong"
    EmployeeCode[12] = "S004"
    Surname[12] = "Ang"
    EmployeeCode[13] = "S005"
    Surname[13] = "Wong"
    EmployeeCode[14] = "S006"
    Surname[14] = "Teo"
    EmployeeCode[15] = "S007"
    Surname[15] = "Ho"
    EmployeeCode[16] = "S008"
    Surname[16] = "Chong"
    EmployeeCode[17] = "S009"
    Surname[17] = "Low"
    EmployeeCode[18] = "S010"
    Surname[18] = "Sim"
    EmployeeCode[19] = "S011"
    Surname[19] = "Tay"
    EmployeeCode[20] = "S012"
    Surname[20] = "Tay"
    EmployeeCode[21] = "S013"
    Surname[21] = "Chia"
    EmployeeCode[22] = "S014"
    Surname[22] = "Tan"
    EmployeeCode[23] = "S015"
    Surname[23] = "Yeo"
    EmployeeCode[24] = "S016"
    Surname[24] = "Lim"
    EmployeeCode[25] = "S017"
    Surname[25] = "Tan"
    EmployeeCode[26] = "S018"
    Surname[26] = "Ng"
    EmployeeCode[27] = "S018"
    Surname[27] = "Lim"
    EmployeeCode[28] = "S019"
    Surname[28] = "Toh"
    EmployeeCode[29] = "N011"
    Surname[29] = "Morris"
    EmployeeCode[30] = "N013"
    Surname[30] = "Williams"
    EmployeeCode[31] = "N016"
    Surname[31] = "Chua"
    EmployeeCode[32] = "N023"
    Surname[32] = "Wong"

    printMenu()
    choice = int(input("Choose an option (1-3): "))
    while choice != 3:
        if choice == 1:  # Surname
            searchTerm = input("Enter the surname: ")
            result = search(Surname, EmployeeCode, searchTerm, True)

            if not result:
                print('No matching employee!\n')
            else:
                print("Employee IDs: ", end='')
                for id in result:
                    print(id, end='  ')
                for i in range(2): print()

        elif choice == 2:  # ID
            searchTerm = input("Enter the employee code (A999): ")
            if not (len(searchTerm) == 4 and
                    searchTerm[0].isupper() and
                    searchTerm[-3:].isdigit()):
                print("Invalid code format!")
            else:
                result = search(EmployeeCode, Surname, searchTerm)
                if not result:
                    print('No matching employee!\n')
                else:
                    print('Surname:', result[0])
                    print()

        else:
            print("Invalid option!")

        printMenu()
        choice = int(input("Choose an option (1-3): "))


main()
