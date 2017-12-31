# Falsy Bouncer
# Remove all falsy values from an array.

def bouncer(arr):
  return list(filter(lambda x: x, arr))

#TESTS
print (bouncer([7, "ate", "", False, 9])) #should return [7, "ate", 9].
print (bouncer(["a", "b", "c"])) #should return ["a", "b", "c"].
print (bouncer([False, None, 0, [], set(), ""])) #should return [].
print (bouncer([1, None, False, 2, []])) #should return [1, 2].
