num = 153
tempnum = num
armnum = 0
len = len(str(num))

while tempnum!=0:
    temp = tempnum % 10
    armnum = armnum + (temp**len)
    tempnum = tempnum // 10

print(armnum)

if armnum == num:
    print("Armstrong")
