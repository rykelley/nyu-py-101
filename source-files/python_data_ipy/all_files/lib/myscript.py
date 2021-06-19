

import mymod

print('the value of pi is ', mymod.PI)

print('here are the first 10 prime numbers: ')

for num in mymod.primelist:
    print(num)


print("here's the value of pi doubled: ")

dval = mymod.doubleit(mymod.PI)

print(dval)

