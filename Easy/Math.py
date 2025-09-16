#1.   Fizz Buzz
def fizzBuzz(self, n: int) -> List[str]:
    endResult = []
    for i in range(1,n+1):
        if ((i%5) == 0) and ((i%3) == 0):
            endResult.append("FizzBuzz")
        elif ((i%3) == 0):
            endResult.append("Fizz")
        elif ((i%5) == 0):
            endResult.append("Buzz")
        else:
            endResult.append(str(i))
    
    return endResult

#3.  Power of Three

def isPowerOfThree(self, n: int) -> bool:
    res = False
    if n <= 0:
        return False
    while n%3 == 0:
        n //= 3
    return n == 1 