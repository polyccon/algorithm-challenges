function findElement(arr, func) {

  var array = arr.filter( function(item) {
    if (func(item)){
      return item;
    }
  });
  if (array.length !== 0){
    return array[0];
  }else{
  return undefined;
  }
}

findElement([1, 2, 3, 4], function(num){ return num % 2 === 0; });
findElement([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; }) should return 8.
findElement([1, 3, 5, 9], function(num) { return num % 2 === 0; }) should return undefined.
