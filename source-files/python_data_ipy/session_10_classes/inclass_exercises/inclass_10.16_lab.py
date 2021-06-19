# 10.16:  Update Counter with a show_value() method that
# returns the attribute value.

import runreport

class Counter:
    def __init__(self, val):
        self.counterval = val

    def increment(self):
        self.counterval = self.counterval + 1

    # your code here


c = Counter(5)

c.increment()
c.increment()

print(c.counterval)    # 7


# Expected Output:

# 7

