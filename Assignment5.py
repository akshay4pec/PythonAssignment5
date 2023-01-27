#QUES1
STRING=str(input("the name of string is: "))
STRING1=STRING[::-1]
print(STRING1)



#QUES2
a=int(input("range:"))
b=int(input("User Number:"))
for i in range(a):
    if i%b==0:
        print(i)
        continue
 



#ANS3
a = int(input("Enter the first length: "))
b = int(input("Enter the second length: "))
c = int(input("Enter the third length: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Yes")   
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print('The area of the triangle is %0.2f' %area)  
else:
    print("No") 
    
    
    
    
#ANS4
n=int(input("No. of Rows: "))
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
    
    
#ANS5
n=int(input("No. of Rows: "))
x=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(x), end="")
        x=x+1
    print('')
