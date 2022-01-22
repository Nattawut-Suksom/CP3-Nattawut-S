S
rowInput = int(input("Row of Star:"))
text = ""
empty = ""
for i in range(rowInput):
    text = 1+(2*i)
    text1 = text*"*"
    empty = int((((rowInput*2)-1)-(text))/2)
    empty1 = (empty)*" "

    print(empty1,text1,empty1)