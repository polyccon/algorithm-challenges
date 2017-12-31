#Seek and destroy
# Remove all elements from the initial array that are of the same value as these arguments.
# Note: this is a slight alteration of the JS version
# *args is for unknown arguments of variable length


def destroyer(arr, *args):
  return [x for x in arr if x not in args]

#TESTS
print (destroyer([1, 2, 3, 1, 2, 3], 2, 3)) #should return [1, 1].
print (destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3)) #should return [1, 5, 1].
print (destroyer([3, 5, 1, 2, 2], 2, 3, 5)) #should return [1].
print (destroyer([2, 3, 2, 3], 2, 3)) #should return [].
print (destroyer(['tree', 'hamburger', 53], 'tree', 53)) #should return ["hamburger"].
