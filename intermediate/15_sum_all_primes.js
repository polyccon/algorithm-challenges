//Sum all the prime numbers up to and including the provided number.

//A prime number is defined as a number greater than one and having only two divisors, one and itself. For example, 2 is a prime number because it's only divisible by one and two.

//The provided number may not be a prime.

function isPrime(x){
      d = x-1;
      while (d > 1){
        if ((x % d) === 0) return false;
        d--;
      }
      return true;
    }

function sumPrimes(num) {
  var sum = 0;
  var count = 1;

  while (count<=num-1){
    count ++;
    if (isPrime(count)){
      sum += count;
    }
  }

  return sum;
}


sumPrimes(10); //should return a number.
sumPrimes(10); //should return 17.
sumPrimes(977); //should return 73156.
