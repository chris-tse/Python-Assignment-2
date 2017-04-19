# As written in class
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

# As written in class
def Primes():
    yield 2 
    i = 3
    while (True):
        if is_prime(i):
            yield i
        i += 2

def Threes():
    n = 1
    while(True):
        yield 3 ** n
        n += 1

def interesting(n): 
    for i in Primes():
        for j in Threes():
            if i + j > n:
                yield i+j
    return 0
input = 113366623 * 10 
count = 0
for i in interesting(input):
    if count > 20:
        break
    print(i)
    count += 1

