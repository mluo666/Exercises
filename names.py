print("====================")
print("     Name System    ")
print("1: add a name")
print("2: delete a name")
print("3: modify a name")
print("4: search a name")
print("====================")
choice = int(raw_input("Please enter your choice:"))
nameList = []

def addName(name,nameList):
    newNameList = nameList.append(name)
    return newNameList

def deleteName(name,nameList):
    findResult = findName(name,nameList)
    if findResult == 0:
        newNameList = nameList.remove(name)
        return newNameList
    else:
        print("It is not excited.")

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
        return 0
    else:
        print("not found!")
        return 1

if choice == 1:
    newName = raw_input("Please enter a name to add:")
    print("================")
    newNameList = addName(newName,nameList)
    print(nameList)
    print(newNameList)
elif choice == 2:
    delName = raw_input("Please enter a name to delete:")
    newNameList = deleteName(delName,nameList)
    print(nameList)
    print(newNameList)
elif choice == 3:
    modName = raw_input("Please enter a name to modify:")
    newNameList = modifyName(modName,nameList)
    print(nameList)
    print(newNameList)
elif choice == 4:
    searchName = raw_input("Please enter a name to find:")
    newNameList = findName(searchName,nameList)
    print(nameList)
    print(newNameList)
else:
    print("Please enter a valid number!")
