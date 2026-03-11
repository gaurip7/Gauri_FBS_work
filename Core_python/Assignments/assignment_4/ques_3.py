# WAP to print sum of series upto n.

num = int(input('Enter the number: '))
sum = 0
for i in range(1,num+1):
    sum += i                    
print('Sum of series of n number: ',sum)