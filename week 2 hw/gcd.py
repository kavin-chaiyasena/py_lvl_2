import time as tm
def gcd(x, y) :
    d = 1000
    while True :
        if x % d == 0 and y % d == 0 :
            break
        else :
            d = d-1
    return d
t1 = tm.time()
print(gcd(88,11))
t2 = tm.time()
print(round(t2 - t1, 8))