# 2.17:  While loop until arbitrary value.  Add a test so that
# this while loop continues looping until the user's input is
# equal to 'yes'.

# (Note if you can't get out of a loop, in PyCharm use the red
# square to the left of the Run window; in Jupyter notebook,
# restart the kernel.)

# continue looping until input is equal to 'yes'
ui = ''

while ui != 'yes':
    # your test here

    ui = input("please say yes, otherwise I'll ask again: " )





print('done')

# Expected Output:

# please say yes, otherwise I'll ask again: no
# please say yes, otherwise I'll ask again: well
# please say yes, otherwise I'll ask again: what
# please say yes, otherwise I'll ask again: yes
# done

