# Initialize ID number for ease of testing
ID = 112971666

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


# Generates powers of 3 starting from 3 ^ 1
def Threes():
    n = 1
    while(True):
        yield 3 ** n
        n += 1

# Function to check for interesting numbers
# Sequentially checks numbers after n and subtracts
# powers of 3 and checks if difference is prime
def interesting(n):

    test = n + 1

    while(True):

        for i in Threes():
            j = test - i

            if i >= test:
                test += 1
                break

            elif is_prime(j):
                yield test
                test += 1
                break

# Test driver for interesting function
# N: Starting value
# times: Number of values to print out
def test_interesting(N, times):
    count = 0

    for i in interesting(N):
        if count == times:
            break
        print(i)
        count += 1

