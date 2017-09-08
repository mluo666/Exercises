# Question 3

nameList = []

def addNameCard():
    namecards = {}
    newName = raw_input("Please enter a new name:")
    namecards["name"] = newName
    newTelNum = raw_input("Please enter a new tel number:")
    namecards["Tel"] = newTelNum
    return namecards

def delNameCard(nameList):
    delName = raw_input("Please enter a name to delete:")
    for namecards in nameList:
        if namecards.get("name") == delName:
            nameList.remove(namecards)
    return nameList

def modNameCard(nameList):
    modName = raw_input("Please enter a name to modify:")
    for namecards in nameList:
        if namecards.get("name") == modName:
            newTel = raw_input("Please enter a new tel number:")
            namecards["Tel"] = newTel
    return

def findNameCard(nameList):
    flag = 0
    findName = raw_input("Please enter a name to find:")
    for namecards in nameList:
        if namecards.get("name") == findName:
            print("Find!")
            flag = 1
    if flag == 0:
        print("not existed!")

while 1:
    print("=================")
    print("Name Card System")
    print("1. add a name card")
    print("2. delete a name card")
    print("3. modify a name card")
    print("4. search a name card")
    print("5. exit")
    print("=================")
    choice = int(raw_input("Please choose a number:"))

    if choice == 1:
        newNamecards = addNameCard()
        nameList.append(newNamecards)
        print(nameList)

    elif choice == 2:
        delNameCard(nameList)
        print(nameList)

    elif choice == 3:
        modNameCard(nameList)
        print(nameList)

    elif choice == 4:
        findNameCard(nameList)
        print(nameList)

    elif choice == 5:
        break
    else:
        print("Please enter a valid number!")