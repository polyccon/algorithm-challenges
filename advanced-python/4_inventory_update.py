# Inventory Update
'''
Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery.
Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the
new item and quantity into the inventory array. The returned inventory array should be in alphabetical order by item.
'''
def takeSecond(elem):
    return elem[1]

def updateInventory(arr1, arr2):
    # All inventory must be accounted for or you're fired!
  for array2 in arr2:
    for array1 in arr1:
      if array1[1] is array2[1]:
        array1[0] += array2[0]
    if all(arr1[i][1] is not array2[1] for i in range(len(arr1))):
        arr1.append(array2)
  return sorted(arr1, key=takeSecond)
 

 print (len(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"],
 [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"],
 [7, "Toothpaste"]])))
# should return an array with a length of 6.

print (updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"],
[5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"],
[7, "Toothpaste"]]))
#should return [[88, "Bowling Ball"], [2, "Dirty Sock"], [3, "Hair Pin"], [3, "Half-Eaten Apple"],
#[5, "Microphone"], [7, "Toothpaste"]]).
print (updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"],
[5, "Microphone"]], []))
#should return [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]].
print (updateInventory([], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"],
[7, "Toothpaste"]]))
#should return [[67, "Bowling Ball"], [2, "Hair Pin"], [3, "Half-Eaten Apple"], [7, "Toothpaste"]].
print (updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"],
[0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"],
[1, "Toothpaste"]]))
#should return [[1, "Bowling Ball"], [0, "Dirty Sock"], [1, "Hair Pin"], [1, "Half-Eaten Apple"],
#[0, "Microphone"], [1, "Toothpaste"]].
