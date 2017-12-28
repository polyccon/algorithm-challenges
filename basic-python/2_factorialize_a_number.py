#Factorialise a Number
#Return the factorial of the provided integer.
#If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.
#Factorials are often represented with the shorthand notation n!

#For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorialize(num):
  fact = 1
  i = 1

  if num == 0:
    num += 1
  while i<num:
    fact *= i
    i+=1
  return fact*num

print (factorialize(5)) #should return a number.
print (factorialize(5)) #should return 120.
print (factorialize(10)) #should return 3628800.
print (factorialize(20)) #should return 2432902008176640000.
print (factorialize(0)) #should return 1.
