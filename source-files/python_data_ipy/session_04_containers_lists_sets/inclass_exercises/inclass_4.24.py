# 4.24:  Compare a tuple to a list.

# Given the below code which shows several operations that are
# possible with a list, change the list to a tuple (replace
# the square brackets with parentheses in the first line) and
# re-run the code to see what operations may be possible with
# a tuple.
# 
# (Note:  spaces inside {} are included for clarity.)

myseq = [3, 1, 5, 9, 7, 11]

print(f'the sequence:  {  myseq  }')

print(f'last item:     {  myseq[-1]  }')

print(f'first 3 items: {  myseq[0:3] }')

print(f'last 3 items:  {  myseq[-3:]  }')

print(f'# of items:    {  len(myseq) }')

print(f'maximum value: {  max(myseq) }')

print(f'minimum value: {  min(myseq) }')

print('each item in sequence:')
for item in myseq:
    print(item)
print()

print(f'sorted:        {  sorted(myseq)  }')

print('appending to sequence: ')
myseq.append(99)
print(myseq)

