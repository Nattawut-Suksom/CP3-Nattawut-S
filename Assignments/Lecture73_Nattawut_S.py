
menuList = []
menuDict = {"pizza":50,"burger":30,"lime":70}

while True:
    menuInput = input("Please Enter Menu:")
    if menuInput.lower() == "exit":
        break
    else:
        menuList.append([menuInput,menuDict[menuInput]])

def bilList():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])

def totalPrice():
    total = 0
    for i in range(len(menuList)):
        total = total + int(menuList[i][1])
    print("total:",total,"บาท")

bilList()
totalPrice()