#fibonacci series
n= int(input("Enter the number of term :"))
a, b= 0,1
for i in range(n):
 print(a,end="")
 a, b=b,a+b
