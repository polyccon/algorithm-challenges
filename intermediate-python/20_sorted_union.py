from functools import reduce

def uniteUnique(*arr):

  onearr = reduce((lambda x, y: x + y), arr)
  '''
  I tried to then return set(onearr)
  and got: TypeError: unhashable type: 'list'
  with bit of research for unhashable types (e.g. list of lists), 
  and methods that preserve the order of the original lists:
  '''
  seen = set()
  return [ x for x in onearr if str( x ) not in seen and not seen.add( str( x ) )]

 #TESTS
print (uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]))
#should return [1, 3, 2, 5, 4].
print (uniteUnique([1, 3, 2], [1, [5]], [2, [4]]))
#should return [1, 3, 2, [5], [4]].
print (uniteUnique([1, 2, 3], [5, 2, 1]))
#should return [1, 2, 3, 5].
print (uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]))
#should return [1, 2, 3, 5, 4, 6, 7, 8].

# More info: https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-whilst-preserving-order
