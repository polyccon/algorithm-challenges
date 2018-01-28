import math

def createDict(dict):
  GM = 398600.4418
  earthRadius = 6367.4447
  a = round(earthRadius)
  return { 'name': dict['name'],
    'orbitalPeriod': round(2 *math.pi *math.sqrt((a + round(dict['avgAlt']))**3/ GM))}

def orbitalPeriod(arr):
  return list(map(createDict, arr))

#TESTS
print (orbitalPeriod([{'name' : "sputnik", 'avgAlt' : 35873.5553}]))
#should return [{name: "sputnik", orbitalPeriod: 86400}].
print (orbitalPeriod([{'name': "iss", 'avgAlt': 413.6}, {'name': "hubble", 'avgAlt': 556.7},
{'name': "moon", 'avgAlt': 378632.553}]))
#should return [{name : "iss", orbitalPeriod: 5557}, {name: "hubble", orbitalPeriod: 5734},
#{name: "moon", orbitalPeriod: 2377399}].
