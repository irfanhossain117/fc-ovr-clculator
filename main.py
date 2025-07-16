import math



num1=input("Enter How many Player you have In Your Team :")
num2=input("Input Base Ovr :")
num3=input("Input Rank up Ovr :")




num1=int(num1)
num2=int(num2)
num3=int(num3)

div1=num2/num1
div2=num3/num1
sum=div1+div2




print(math.ceil(sum))

#print(math.floor(sum))

#print(round(sum))