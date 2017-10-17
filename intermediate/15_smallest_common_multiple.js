// Find the smallest common multiple of the provided parameters that can be evenly divided by both,
//as well as by all sequential numbers in the range between these parameters.

//The range will be an array of two numbers that will not necessarily be in numerical order.

//e.g. for 1 and 3 - find the smallest common multiple of both 1 and 3 that is evenly divisible
//by all numbers between 1 and 3.

function isCommonMultiple(array, number){
    var arraytf = array.map(function(x){
        return number%x === 0;});

    var par = arraytf.reduce(function(a,b){
      if (a===b){
        return a;
      }else{
        return false;
      }});
    return par;
  }

function smallestCommons(arr) {
  var min = Math.min.apply(null, arr);
  var max = Math.max.apply(null, arr);

  var plus = min;
  var array = [];

    while(plus <max+1){
      array.push(plus);
      plus++;
    }

  var times = 1;
  var mult = max;

    while (!isCommonMultiple(array, mult)){
      mult =times*max;
      times++;
    }
    return mult;
}

smallestCommons([1, 5]); // should return a number.
smallestCommons([1, 5]); // should return 60.
smallestCommons([5, 1]); // should return 60.
smallestCommons([1, 13]); // should return 360360.
smallestCommons([23, 18]); // should return 6056820.
