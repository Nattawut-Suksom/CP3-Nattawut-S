
priceInput = int(input("กรุณาใส่ราคาสินค้า:"))
def vatCalculator(price):
    totalPrice = price+(price*(7/100))
    return totalPrice

print("ราคาสินค้ารวม Vat:",vatCalculator(priceInput),"บาท")