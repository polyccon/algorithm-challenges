# Mutations
# Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.
# For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.
# The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".
# Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".

# remove duplicates
def removedupl(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def mutation(arr):
  arr0 = []
  arr1 = []

  # Could not use the ".split("")" method with an empty separator like in JS,
  # so I found the following method instead which is a way to add items in a list.
  # Note: arr += [item] will add "item" as one in list "arr"

  arr0 += arr[0].lower()
  arr1 += arr[1].lower()

  arr0 = removedupl(arr0)
  arr1 = removedupl(arr1)

  if len(arr0) == len(arr1):
    return True

  for i in arr1:
    if ''.join(arr0).find(i) == -1:
      return False
  return True


# TESTS
print (mutation(["hello", "hey"])) #should return false.
print (mutation(["hello", "Hello"])) #should return true.
print (mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])) #should return true.
print (mutation(["Mary", "Army"])) #should return true.
print (mutation(["Mary", "Aarmy"])) #should return true.
print (mutation(["Alien", "line"])) #should return true.
print (mutation(["floor", "for"])) #should return true.
print (mutation(["hello", "neo"])) #should return false.
print (mutation(["voodoo", "no"])) #should return false.
