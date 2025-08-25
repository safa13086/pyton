num=121
num2=""
str1=str(num)
for i in range(len(str1)-1,-1,-1):
    num2+=str1[i]
print(num2)
if str1==num2:
    print("it is a palindrom")
else:
    print("it is not a palindrom")
    
    
