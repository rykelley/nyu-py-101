# 10.3:  Copy the previous code, and this time replace the
# set_time() method with the constructor, __init__(self),
# which does the same work - sets the attribute to the current
# timestamp.  Now the method has only an __init__(self) method
# and a get_time(self) method which returns the timestamp.

# Expected calls and output (your timestamp will differ of
# course, but note when the object time is repeated and when
# it is different):

# your class here

var1 = TimeStamp()
var2 = TimeStamp()
print(var1.get_time())    # 2013-04-07 15:19:31.762220
print(var2.get_time())    # 2013-04-07 15:19:31.956881
print()
print(var1.get_time())    # 2013-04-07 15:19:31.762220
                         # (same as previous var1)
print(var2.get_time())    # 2013-04-07 15:19:31.956881
                         # (same as previous var2)

