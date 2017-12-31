# Falsy Bouncer
# Remove all falsy values from an array.
# Falsy values in Python ar: None, False, 0, 0.0, 0j, [], {}, (), '', set()
 # and objects for which:
#    obj.__bool__() returns False
#    obj.__len__() returns 0


def bouncer(arr):
  return list(filter(lambda x: x, arr))

# OR

def bouncer(arr):
  return [x for x in arr if x]
  
#TESTS
print (bouncer([7, "ate", "", False, 9])) #should return [7, "ate", 9].
print (bouncer(["a", "b", "c"])) #should return ["a", "b", "c"].
print (bouncer([False, None, 0, [], set(), ""])) #should return [].
print (bouncer([1, None, False, 2, []])) #should return [1, 2].
