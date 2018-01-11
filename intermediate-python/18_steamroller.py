#STEAMROLLER
#Flatten a nested array. You must account for varying levels of nesting.

from functools import reduce

def flat(acc, cur):
  if type(cur) == type([]):
    acc.extend(cur)
  else:
    acc.append(cur)
  return acc

def flattenManyToOne(array):
  return reduce(flat, array, [])

def flattenOneToOne(item):
  while type(item) == type([]):
    item = item[0]
  return item

# OR using recursion:
def flattenOneToOne(item):
  if type(item) != type([]):
    return item
  else:
    return flattenOneToOne(item[0])

def steamrollArray(array):
  return list(map(flattenOneToOne, flattenManyToOne(array)))


#Tests
print (steamrollArray([['a']])) #should return ['a']
print (steamrollArray([[['a']], [['b']]])) #should return ["a", "b"].
print (steamrollArray([1, [2], [3, [[4]]]])) #should return [1, 2, 3, 4].
print (steamrollArray([1, [], [3, [[4]]]])) #should return [1, 3, 4].
print (steamrollArray([1, {}, [3, [[4]]]])) #should return [1, {}, 3, 4].
