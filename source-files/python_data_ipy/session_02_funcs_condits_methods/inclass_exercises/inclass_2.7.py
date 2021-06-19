# 2.7:  Use 'not' to negate a test.

# Use not in front of the in operator to see if user's input
# is not in the sentence.  If cannot be found there, print not
# found.

text = 'Calculation is the name of the game.  '

num = input('please enter search text:  ')

if not num in text:
    print('not found')
