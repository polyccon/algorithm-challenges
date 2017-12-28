#Title Case a Sentence
# Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.
# For the purpose of this exercise, you should also capitalize connecting words like "the" and "of".

def titleCase(str):
  array = str.lower().split(' ')
  arrUpper =[];

  for word in array:
    arrUpper.append(word[0].upper() + word[1:])
  return ' '.join(arrUpper)

print (titleCase("I'm a little tea pot")) #should return a string.
print (titleCase("I'm a little tea pot")) #should return "I'm A Little Tea Pot".
print (titleCase("sHoRt AnD sToUt")) #should return "Short And Stout".
print (titleCase("HERE IS MY HANDLE HERE IS MY SPOUT")) #should return "Here Is My Handle Here Is My Spout".
