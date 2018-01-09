# PIG LATIN
'''
Translate the provided string to pig latin.
Pig Latin takes the first consonant (or consonant cluster) of an English word,
moves it to the end of the word and suffixes an "ay".
If a word begins with a vowel you just add "way" to the end.
Input strings are guaranteed to be English words in all lowercase.
'''

def isVowel(char):
   return any ((char == "a", char == "o", char == "e", char == "i", char == "u"))

def firstvowelindex (str):
  for i in range(0, len(str)+1):
    if isVowel(str[i]):
       return i
  return 0

def translatePigLatin(str):

  if isVowel(str[0]):
    return str+'way'
  else:
    i = firstvowelindex(str)
    return str[i: len(str)]+str[0:i]+'ay'

#TESTS
print (translatePigLatin("california")) #should return "aliforniacay".
print (translatePigLatin("paragraphs")) #should return "aragraphspay".
print (translatePigLatin("glove")) #should return "oveglay".
print (translatePigLatin("algorithm")) #should return "algorithmway".
print (translatePigLatin("eight")) #should return "eightway".
