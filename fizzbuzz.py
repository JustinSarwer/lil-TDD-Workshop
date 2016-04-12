def fizzbuzz(n):
    divisBy3 = n % 3 == 0
    divisBy5 = n % 5 == 0

    if(divisBy3 and divisBy5):
        return "FizzBuzz"
    if(divisBy3):
        return "Fizz"
    if(divisBy5):
        return "Buzz"
    return n