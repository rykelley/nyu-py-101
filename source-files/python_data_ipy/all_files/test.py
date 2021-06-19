fh = open('revenue.txt')    # a 'file' object
fsum = 0.0
for line in fh:             # 'The Store,NJ,211.50'
    items = line.split(',') # ['The Store', 'NJ', '211.50\n']
    val = items[2]          # '211.50\n'
    fval = float(val)       # 211.50
    fsum = fsum + fval
print(fsum)
