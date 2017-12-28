#REVERSE A STRING
# Reverse the provided string.
# You may need to turn the string into an array before you can reverse it.
# Your result must be a string.

def reverseString(str):
    return str[::-1] #This is extended slice syntax. It works by doing [begin:end:step] -
    #by leaving begin and end off and specifying a step of -1, it reverses a string.

# OR
def reverseString(str):
    return ''.join(reversed(str))
# TESTS
print (reverseString("hello")) #should return a string.
print (reverseString("hello")) #should become "olleh".
print (reverseString("Howdy")) #should become "ydwoH".
print (reverseString("Greetings from Earth")) #should return "htraE morf sgniteerG"
