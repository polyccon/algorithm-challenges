# EVERYTHING BE TRUE
# Check if the predicate (second argument) is truthy on all elements of a collection
# (first argument).

def truthCheck(collection, pre):
  # Is everyone being true?
  return all(object.get(pre) for object in collection)

#TESTS
print (truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex")) #should return true.
print (truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex")) #should return false.
print (truthCheck([{"user": "Tinky-Winky", "sex": "male", "age": 0}, {"user": "Dipsy", "sex": "male", "age": 3}, {"user": "Laa-Laa", "sex": "female", "age": 5}, {"user": "Po", "sex": "female", "age": 4}], "age")) #should return false.
print (truthCheck([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True}, {"name": "FastFoward", "onBoat": None}], "onBoat")) #should return false
print (truthCheck([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True, "alias": "Repete"}, {"name": "FastFoward", "onBoat": True}], "onBoat")) #should return true
print (truthCheck([{"single": "yes"}], "single")) #should return true
print (truthCheck([{"single": ""}, {"single": "double"}], "single")) #should return false
print (truthCheck([{"single": "double"}, {"single": None}], "single")) #should return false
print (truthCheck([{"single": "double"}, {"single": None}], "single")) #should return false
