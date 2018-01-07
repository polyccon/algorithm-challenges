# SUM ALL NUMBERS IN A RANGE
# We'll pass you an array of two numbers.
# Return the sum of those two numbers and all numbers between them.

#The lowest number will not always come first.

def sumAll(arr):
  return sum(x for x in range(min(arr), max(arr)+1))

#TESTS
print (sumAll([1, 4])) #should return a number.
print (sumAll([1, 4])) #should return 10.
print (sumAll([4, 1])) #should return 10.
print (sumAll([5, 10])) #should return 45.
print (sumAll([10, 5])) #should return 45.
