# Write a program to print prime numbers between 1 to 100.

num = int(input('Enter the number till prime number you want to print: '))
for n in range(2,num):        
    for i in range(2,n):          
        if (n % i) == 0:
            break
    else:
        print(n)                 