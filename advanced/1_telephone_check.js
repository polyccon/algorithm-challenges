function telephoneCheck(str) {
  if (
    str.length > 16 ||
    str.length === 15 ||
    str.length < 10 ||
    str.length === 11
  ) {
    return false;
  } else if (str.length === 10 && /\D/.test(str)) {
    return false;
  } else if (
    str.length === 12 &&
    !((str[3] === '-' && str[7] === '-') || (str[3] === ' ' && str[7] === ' '))
  ) {
    return false;
  } else if (
    str.length === 13 &&
    !(str[0] === '(' && str[4] === ')' && (str[8] === '-' || str[8] === ' '))
  ) {
    return false;
  } else if ((str.length === 14 || str.length === 16) && str[0] !== '1') {
    return false;
  } else if (
    str.length === 14 &&
    ((str[1] === '(' && str[5] != ')') || (str[1] !== '(' && str[5] === ')'))
  ) {
    return false;
  }
  return true;
}

// TESTS
console.log(telephoneCheck('555-555-5555')); //should return true.
console.log(telephoneCheck('1 555-555-5555')); //should return true.
console.log(telephoneCheck('1 (555) 555-5555')); //should return true.
console.log(telephoneCheck('5555555555')); //should return true.
console.log(telephoneCheck('55555/5555')); //should return false.
console.log(telephoneCheck('555-555-5555')); //should return true.
console.log(telephoneCheck('(555)555-5555')); //should return true.
console.log(telephoneCheck('1(555)555-5555')); //should return true.
console.log(telephoneCheck('555-5555')); //should return false.
console.log(telephoneCheck('5555555')); //should return false.
console.log(telephoneCheck('1 555)555-5555')); //should return false.
console.log(telephoneCheck('1 555 555 5555')); //should return true.
console.log(telephoneCheck('1 456 789 4444')); //should return true.
console.log(telephoneCheck('123**&!!asdf#')); //should return false.
console.log(telephoneCheck('55555555')); //should return false.
console.log(telephoneCheck('(6505552368)')); //should return false
console.log(telephoneCheck('2 (757) 622-7382')); //should return false.
console.log(telephoneCheck('0 (757) 622-7382')); //should return false.
console.log(telephoneCheck('-1 (757) 622-7382')); //should return false
console.log(telephoneCheck('2 757 622-7382')); //should return false.
console.log(telephoneCheck('10 (757) 622-7382')); //should return false.
console.log(telephoneCheck('27576227382')); //should return false.
console.log(telephoneCheck('(275)76227382')); //should return false.
console.log(telephoneCheck('2(757)6227382')); //should return false.
console.log(telephoneCheck('2(757)622-7382')); //should return false.
console.log(telephoneCheck('555)-555-5555')); //should return false.
console.log(telephoneCheck('(555-555-5555')); //should return false.
console.log(telephoneCheck('(555)5(55?)-5555')); //should return false.
