function updateInventory(arr1, arr2) {
  // All inventory must be accounted for or you're fired!
  arr2.forEach(function(array2, ind) {
    arr1.forEach(function(array1) {
      if (array1[1] === array2[1]) {
        array1[0] += array2[0];
      }
    });
    if (arr1.every(array1 => array1[1] !== array2[1])) {
      arr1.push(array2);
    }
  });
  return arr1.sort(function(a, b) {
    return a[1] == b[1] ? 0 : a[1] < b[[1]] ? -1 : 1;
  });
  //OR
  //   return arr1.sort(function(a, b){
  //       return a[1].localeCompare(b[1]);
  // })
}

//TESTS
updateInventory(
  [[21, 'Bowling Ball'], [2, 'Dirty Sock'], [1, 'Hair Pin'], [5, 'Microphone']],
  [
    [2, 'Hair Pin'],
    [3, 'Half-Eaten Apple'],
    [67, 'Bowling Ball'],
    [7, 'Toothpaste'],
  ]
).length;
//should return an array with a length of 6.
updateInventory(
  [[21, 'Bowling Ball'], [2, 'Dirty Sock'], [1, 'Hair Pin'], [5, 'Microphone']],
  [
    [2, 'Hair Pin'],
    [3, 'Half-Eaten Apple'],
    [67, 'Bowling Ball'],
    [7, 'Toothpaste'],
  ]
);
//should return [[88, "Bowling Ball"], [2, "Dirty Sock"], [3, "Hair Pin"], [3, "Half-Eaten Apple"], [5, "Microphone"], [7, "Toothpaste"]].
updateInventory(
  [[21, 'Bowling Ball'], [2, 'Dirty Sock'], [1, 'Hair Pin'], [5, 'Microphone']],
  []
);
//should return [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]].
updateInventory(
  [],
  [
    [2, 'Hair Pin'],
    [3, 'Half-Eaten Apple'],
    [67, 'Bowling Ball'],
    [7, 'Toothpaste'],
  ]
);
//should return [[67, "Bowling Ball"], [2, "Hair Pin"], [3, "Half-Eaten Apple"], [7, "Toothpaste"]].
updateInventory(
  [[0, 'Bowling Ball'], [0, 'Dirty Sock'], [0, 'Hair Pin'], [0, 'Microphone']],
  [
    [1, 'Hair Pin'],
    [1, 'Half-Eaten Apple'],
    [1, 'Bowling Ball'],
    [1, 'Toothpaste'],
  ]
);
//should return [[1, "Bowling Ball"], [0, "Dirty Sock"], [1, "Hair Pin"], [1, "Half-Eaten Apple"], [0, "Microphone"], [1, "Toothpaste"]].
