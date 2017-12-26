//STEAMROLLER
//Flatten a nested array. You must account for varying levels of nesting.

const flattenManyToOne = array =>
  array.reduce((acc, cur) => acc.concat(cur), []);

const flattenOneToOne = item => {
  while (Array.isArray(item)) {
    item = item[0];
  }
  return item;
};

const steamrollArray = array => {
  return flattenManyToOne(array).map(flattenOneToOne);
};

//Tests
steamrollArray([[['a']], [['b']]]); //should return ["a", "b"].
steamrollArray([1, [2], [3, [[4]]]]); //should return [1, 2, 3, 4].
steamrollArray([1, [], [3, [[4]]]]); //should return [1, 3, 4].
steamrollArray([1, {}, [3, [[4]]]]); //should return [1, {}, 3, 4].
