#Find the Longest Word in a String

#Return the length of the longest word in the provided sentence.
# Your response should be a number.

def findLongestWord(str):
  array = str.split(' ')
  arraylength = []
  for word in array:
     arraylength.append(len(word))
  return max(arraylength)

print (findLongestWord("The quick brown fox jumped over the lazy dog")) #should return a number.
print (findLongestWord("The quick brown fox jumped over the lazy dog")) #should return 6.
print (findLongestWord("May the force be with you")) #should return 5.
print (findLongestWord("Google do a barrel roll")) #should return 6.
print (findLongestWord("What is the average airspeed velocity of an unladen swallow")) #should return 8.
print (findLongestWord("What if we try a super-long word such as otorhinolaryngology")) #should return 19.
