def filt(array1, array2):
  arr = []
  for item in array1:
    if item not in array2:
      arr.append(item)
  return arr

def diffArray(arr1, arr2):
  return filt(arr1, arr2) + filt(arr2, arr1)

#TESTS
print (diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5])) #should return an array.
print (diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])) #should return ["pink wool"].
print (diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])) #should return ["pink wool"].
print (diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])) #should return ["diorite", "pink wool"].
print (diffArray(["andesite", "grass", "dirt", "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"])) #should return [].
print (diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5])) #should return [4].
print (diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4])) #should return ["piglet", 4].
print (diffArray([], ["snuffleupagus", "cookie monster", "elmo"])) #should return ["snuffleupagus", "cookie monster", "elmo"].
print (diffArray([1, "calf", 3, "piglet"], [7, "filly"])) #should return [1, "calf", 3, "piglet", 7, "filly"].
