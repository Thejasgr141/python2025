def sum_of_squares(n):
 return sum(i**2 for i in range (1,n+1))
N=int(input("Enter a number:"))
print("Sum of squares of first",N,"natural number is:",sum_of_squares(N))
