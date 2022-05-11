from tkinter import *
import math

def leftClick(event):
    weightBox = float(boxWeight.get())
    highBox = float(boxHigh.get())
    calBmi = (weightBox/math.pow((highBox/100),2))

    if calBmi >= 30:
        resultBmi = "อ้วนมาก"
    elif calBmi >= 25:
        resultBmi = "อ้วน"
    elif calBmi >= 23:
        resultBmi = "น้ำหนักเกิน"
    elif calBmi >= 18.6:
        resultBmi = "น้ำหนักปกติ"
    elif calBmi <= 18.5:
        resultBmi = "น้ำหนักน้อยเกินไป"
    else:
        resultBmi = "กรุณากรอกข้อมูลใหม่"

    labelCal.configure(text = resultBmi)

mainWindow = Tk()

labelHigh = Label(mainWindow,text = "ส่วนสูง(cm)")
labelHigh.grid(row=0,column=0)

boxHigh = Entry(mainWindow)
boxHigh.grid(row=0,column=1)

labelWeight = Label(mainWindow,text = "น้ำหนัก(kg)")
labelWeight.grid(row=1,column=0)

boxWeight = Entry(mainWindow)
boxWeight.grid(row=1,column=1)

buttonCal = Button(mainWindow,text = "คำนวณ")
buttonCal.bind('<Button-1>',leftClick)
buttonCal.grid(row=2,column=0)

labelCal = Label(mainWindow,text ="bmi")
labelCal.grid(row=2,column=1)
mainWindow.mainloop()
