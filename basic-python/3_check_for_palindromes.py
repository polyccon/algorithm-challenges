import re

# re is the REGEX object which is imported, method strip removes whitespaces
def palindrome(str):
  string = re.sub('[^A-Za-z0-9]+', '', str).strip().lower()
  if string[::-1] == string:
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
