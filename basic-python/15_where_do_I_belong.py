# Where do I belong
# Return the lowest index at which a value (second argument)
# should be inserted into an array (first argument) once it has been sorted.
# The returned value should be a number.

def getIndexToIns(arr, num):
  array = arr[:]
  array.append(num)
  array.sort()
  return array.index(num)

#TESTS
print (getIndexToIns([10, 20, 30, 40, 50], 35)) #should return 3.
print (getIndexToIns([10, 20, 30, 40, 50], 30)) #should return 2.
print (getIndexToIns([40, 60], 50)) #should return 1.
print (getIndexToIns([3, 10, 5], 3)) #should return 0.
print (getIndexToIns([5, 3, 20, 3], 5)) #should return 2.
print (getIndexToIns([2, 20, 10], 19)) #should return 2.
print (getIndexToIns([2, 5, 10], 15)) #should return 3.
