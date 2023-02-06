num = int(input(Enter number   ))
cube = (num*num*num)
print("Cube of" , num,  "is" ,cube)


num= int(input('Enter num.  '))
fact = 1
if num < 0:
    print('Factorial is not possible for negative number')
elif num == 0:
    print('Factorial is zero is 1')
else:
    for i in range(1,num+1):
        fact = fact*i
    print('Factorial is ',fact)
print('Program is done')



