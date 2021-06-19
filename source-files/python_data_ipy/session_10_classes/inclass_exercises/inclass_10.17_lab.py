# 10.17:  Set a class variable, 'increment_value', that
# specifies how much the increment() method should increase
# the attribute.  Add this value to the .counterval attribute
# in increment().

import runreport

class Counter:
    # your class variable here

    def __init__(self, val):
        self.counterval = val

    def increment(self):
        self.counterval = self.counterval + 1
        # add the value of increment_value here

c = Counter(5)

c.increment()
c.increment()

print(c.counterval)    # 5 + (2 * increment_value)

# Expected Output:

# 7

