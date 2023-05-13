import time as tm

def gcd(x, y):
    d = 1000
    while True:
        if x % d == 0 and y % d == 0:
            break
        else:
            d = d - 1
    return d

def lcm(x, y):
    return (x * y) // gcd(x, y)

t1 = tm.time()
print(lcm(12, 30))
t2 = tm.time()
print(round(t2 - t1, 8))
