# Question 1 Name System
nameList = []

def addName(name,nameList):
    nameList = nameList.append(name)
    return nameList

def deleteName(name,nameList):
    findResult = findName(name,nameList)
    if findResult == 1:
        newNameList = nameList.remove(name)
        return newNameList
    elif findResult == 0:
        print("It is not excited.")
    else:
        return

def modifyName(name,nameList):
    if findName(name,nameList) == 1:
        print("not found!")
    else:
        nameList = deleteName(name,nameList)
        newName = raw_input("Please enter a new name:")
        newNameList = addName(newName,nameList)
        return newNameList

def findName(name,nameList):
    if name in nameList:
        print("Find!")
        return 1
    elif name not in nameList:
        print("not found!")
        return 0
    else:
        return

while 1:
    print("====================")
    print("     Name System    ")
    print("1: add a name")
    print("2: delete a name")
    print("3: modify a name")
    print("4: search a name")
    print("5: exit")
    print("====================")
    choice = int(raw_input("Please enter your choice:"))

    if choice == 1:
        newName = raw_input("Please enter a name to add:")
        addName(newName,nameList)
        print(nameList)

    elif choice == 2:
        delName = raw_input("Please enter a name to delete:")
        deleteName(delName,nameList)
        print(nameList)

    elif choice == 3:
        modName = raw_input("Please enter a name to modify:")
        modifyName(modName,nameList)
        print(nameList)

    elif choice == 4:
        searchName = raw_input("Please enter a name to find:")
        findName(searchName,nameList)
        print(nameList)

    elif choice == 5:
        break
    else:
        print("Please enter a valid number!")