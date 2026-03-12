# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


default_userid = 'gauri7'
default_pass = 'gauri123'
for i in range(1,4):
    userid = input('Enter the userid: ')
    password = input('Enter the password: ')
    
    if (userid == default_userid) and (password == default_pass):
        print("You are the right person")
        break
    else:
        print("Invalid Credentials")
        if i == 3:
            print("Account id locked. Program terminated.")