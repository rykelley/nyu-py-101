# 10.1:  Create a class called ThisClass, with one method,
# report(self).  Inside this method, the instance/object
# (which is labeled self) should call the special id()
# function to report its own reference id, i.e. print
# id(self).  Create three instances using the constructor (for
# example, a = ThisClass()) and then call the report() method
# on each of them.

# Lastly, print id() on each of your objects in the calling
# code, for example print id(a).  Note that the id numbers are
# the same as those found when calling report().

# your class here

a = ThisClass()
b = ThisClass()
c = ThisClass()

a.report()          # 4299790736  [your ids will of
                    #              course differ]
b.report()          # 4299790544
c.report()          # 4299790800
print()             # [blank line]

print(id(a))         # 4299790736   (same as a.report() above)
print(id(b))         # 4299790544   (same as b.report() above)
print(id(c))         # 4299790800   (same as c.report() above)

