
usernameInput = input("Username:")
if usernameInput == "customer01":
    print("กรุณาใส่พาสเวิร์ด")
    passwordInput = input("Password:")
    if passwordInput == "5555":
        print("log in success")
        print("*************************")

        print("-------Welcome-------")
        print("*************************")
        print("------รายการสินค้า------")

        mango = 70
        banana = 60
        orange = 90
        print("มะม่วงราคา:", mango, "THB")
        print("กล้วยราคา:", banana, "THB")
        print("ส้มราคา:", orange, "THB")
        print("-----กรุณาเลือกรายการสินค้า-----")

        productInput = input("สินค้าที่เลือก:")
        amountInput = int(input("จำนวนเท่าไหร่:"))

        if productInput == "มะม่วง":
            print("ราคาต่อหน่วย =",mango,"THB")
            print("total =", amountInput*mango,"THB")
        if productInput == "กล้วย":
            print("ราคาต่อหน่วย =",banana,"THB")
            print("total =", amountInput*banana,"THB")
        if productInput == "ส้ม":
            print("ราคาต่อหน่วย =",orange,"THB")
            print("total =", amountInput*orange,"THB")

        print("---THANK YOU---")

    else:
        print("รหัสผ่านผิดพลาด!")
else:
    print("ไม่พบผู้ใช้:",usernameInput)
