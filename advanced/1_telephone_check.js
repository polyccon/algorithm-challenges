// Validate US Telephone Numbers
/*Return true if the passed string is a valid US phone number.

The user may fill out the form field any way they choose as long as it is a valid
US number. The following are examples of valid formats for US numbers (refer to the
tests below for other variants):

555-555-5555
(555)555-5555
(555) 555-5555
555 555 5555
5555555555
1 555 555 5555

For this challenge you will be presented with a string such as:
 800-692-7753 or 8oo-six427676;laskdjf.
 Your job is to validate or reject the US phone number based on any combination
 of the formats provided above. The area code is required. If the country code is
 provided, you must confirm that the country code is
1. Return true if the string is a valid US phone number; otherwise return false.
*/

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

// OR
function telephoneCheck(str) {
  return /^(1|1\s)?(\d{3}|\(\d{3}\))(\s|-)?\d{3}(\s|-)?\d{4}$/.test(str);
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
