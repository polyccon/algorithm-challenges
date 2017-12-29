# Check for Palindromes
# Return true if the given string is a palindrome. Otherwise, return false.
# A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

#Note
#You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything lower case in order to check for palindromes.

#We'll pass strings with varying formats, such as "racecar", "RaceCar", and "race CAR" among others.

# We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2", and "2_A3*3#A2".

import re

# re is the REGEX object which is imported, method strip removes whitespaces
def palindrome(str):
  string = re.sub('[^A-Za-z0-9]+', '', str).strip().lower()
  if string[::-1] == string:
    return True
  return False

# or

PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def palindrome(str):
  str = "".join(c for c in str if c in PERMITTED_CHARS).strip().lower()
  if str[::-1] == str:
    return True
  return False

print (palindrome("eye")) #should return a boolean.
print (palindrome("eye")) #should return true.
print (palindrome("_eye")) #should return true.
print (palindrome("race car")) #should return true.
print (palindrome("not a palindrome")) #should return false.
print (palindrome("A man, a plan, a canal. Panama")) #should return true.
print (palindrome("never odd or even")) #should return true.
print (palindrome("nope")) #should return false.
print (palindrome("almostomla")) #should return false.
print (palindrome("My age is 0, 0 si ega ym.")) #should return true.
print (palindrome("1 eye for of 1 eye.")) #should return false.
print (palindrome("0_0 (: /-\ :) 0-0")) #should return true.
print (palindrome("five|\_/|four")) #should return false.
