# Confirm the Ending
# Check if a string (first argument, str) ends with the given target string (second argument, target).

def confirmEnding(str, target):
  if str[(len(str) - len(target)):]==target:
    return True
  return False

print (confirmEnding("Bastian", "n")) #should return true.
print (confirmEnding("Connor", "n")) #should return false.
print (confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification"))  #should return false.
print (confirmEnding("He has to give me a new name", "name")) #should return true.
print (confirmEnding("Open sesame", "same")) #should return true.
print (confirmEnding("Open sesame", "pen")) #should return false.
print (confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain")) #should return false.
