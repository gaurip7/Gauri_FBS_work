# WAP to check if given number Strong Number.

num = int(input('Enter the number: '))
original_num = num
sum_fact = 0
while num > 0:
    digit = num % 10            
    fact = 1           
    for i in range(1,digit+1):                 
        fact = fact * i
    sum_fact = sum_fact + fact                    
    num = num // 10              
if sum_fact == original_num:         
    print(f'{original_num} is a Strong number.')
else:
    print(f'{original_num} is not a Strong number')