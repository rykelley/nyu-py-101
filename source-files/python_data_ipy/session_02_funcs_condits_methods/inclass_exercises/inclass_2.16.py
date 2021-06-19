# 2.16:  While loop until threshold value.  Increment <\B>num
# until it reaches the value of <\B>threshold.

# (Note if you can't get out of a loop, in PyCharm use the red
# square to the left of the Run window; in Jupyter notebook,
# restart the kernel.)

num = 0
threshold = 3

# your while loop here
while num < threshold:
    print(num)
    num = num + 1
    print('...')

print('done')

# Expected Output:

# 1
# 2
# 3
# 4
# 5
# done

