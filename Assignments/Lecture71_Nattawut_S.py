
menuList = []
priceList = []

while True:
    menuInput = input("Please Enter Menu:")
    if menuInput.lower() == "exit":
        break
    else:
        priceInput = input("Price Enter:")
        menuList.append(menuInput)
        priceList.append(priceInput)

def bilList():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])

def totalPrice():
    total = 0
    for i in range(len(priceList)):
        total = total + int(priceList[i])
    print("total",total,"บาท")
totalPrice()