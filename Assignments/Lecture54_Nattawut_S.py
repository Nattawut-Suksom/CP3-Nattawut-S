
def login():
    usernameInput = input("กรุณาใส่ Username:")
    while usernameInput != "admin":
        usernameInput = input("กรุณาใส่ Username:")
    passwordInput = input("กรุณาใส่ Password:")
    while passwordInput != "5555":
        passwordInput = input("กรุณาใส่ Password:")
    print("----log in success----")
    return True

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * (vat / 100))
    return result

def totalPrice():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    total = price2+price1
    return total

def menu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def selected():
    userSelected = int(input("กรุณาเลือกทำรายการ:"))
    while userSelected != 1 and userSelected != 2:
        userSelected = int(input("กรุณาเลือกทำรายการ:"))
    if userSelected == 1:
        print("ราคาสินค้ารวม vat 7 %:",vatCalculator(totalPrice()),"บาท")
    elif userSelected == 2:
        print("รวมราคาสินค้า:",totalPrice(),"บาท")

login()
menu()
#totalPrice()
#vatCalculator()
selected()
print("---THANK YOU---")
