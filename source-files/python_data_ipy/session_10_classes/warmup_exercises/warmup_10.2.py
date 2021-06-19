# 10.2:  Create a class, TimeStamp(object):  that can store
# the current timestamp in an instance attribute.

# set_time(self): will set the timestamp.  It can do this by
# setting the attribute in self this way (you will need to
# import datetime at the top of your script containing class
# TimeStamp):

self.t = str(datetime.datetime.now())

# where t is the attribute label (you could call it whatever
# you prefer).  (Of course, you'll also need to import
# datetime at the top of your module.)
# 
# get_time(self):  this returns the timestamp.  It simply
# returns the object attribute time, i.e. return self.t.
# 
# Expected calls and output (your timestamp will be different
# of course, but note when the object time is repeated and
# when it is different):

# your class here

var1 = TimeStamp()
var2 = TimeStamp()
var1.set_time()
var2.set_time()
print var1.get_time()    # 2013-04-07 15:19:31.762220
print var2.get_time()    # 2013-04-07 15:19:31.956881
print                    # [blank line]
var1.set_time()          # change timestamp for var1
print(var1.get_time())    # 2013-04-07 15:19:31.956941
                         # (diff from var1 above)
print(var2.get_time())    # 2013-04-07 15:19:31.956881
                         # (same as var2 above)

