
menuList = []

while True:
    menuInput = input("Please Enter Menu:")
    if menuInput.lower() == "exit":
        break
    else:
        priceInput = input("Price Enter:")
        menuList.append([menuInput,priceInput])

def bilList():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i])

def totalPrice():
    total = 0
    for i in range(len(menuList)):
        total = total + int(menuList[i][1])
    print("total:",total,"บาท")

bilList()
totalPrice()