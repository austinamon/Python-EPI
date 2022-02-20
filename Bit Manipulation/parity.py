def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

print(parity(bin(7)))

def isOdd(x):
    return False if x & 1 == 0 else True

print(isOdd(21))


def oppositeSigns(x, y):
    return False if x ^ y > 0 else True

print(oppositeSigns(4, -8))

def negate(x):
    return ~x + 1

print(negate(1))

def addOne(x):
    return -~x 

print(addOne(1))


def swap(x, y):
    print(bin(x))
    print(bin(y))
    x = x ^ y
    print("x ^ y")
    print("x = " + bin(x))
    y = x ^ y
    print("x ^ y")
    print("y = " + bin(y))
    x = x ^ y
    print("x ^ y")
    print(bin(x))
    print(bin(y))

swap(3, 4)