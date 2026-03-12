#  Write a program to solve the following series :
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
sum = 0
sign = 1
den = 1
for i in range(1, n + 1):
    term = sign * (x ** i) / den
    sum = sum + term
    sign = sign * -1
    den = den + 2
print("Sum of series =", sum)