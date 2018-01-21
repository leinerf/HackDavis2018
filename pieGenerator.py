# Greatest common divisor of more than 2 numbers.  Am I terrible for doing it this way?

from functools import reduce

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

# Assuming numbers are positive integers...

a = [{'num':6,'denom':12},{'num':4,'denom':6},{'num':10,'denom':20}]
b = [{'num':6,'denom':12},{'num':4,'denom':6},{'num':10,'denom':20}]
c = [{'num':6,'denom':12},{'num':4,'denom':6},{'num':10,'denom':20}]
def pieGenerator(m, e, s):
    """m is Math, e is English, s is Science"""
     
    mN = 0
    mD = 0
    eN = 0
    eD = 0
    sN = 0
    sD = 0
    
    
    for i in m:
        mN += i['num']
        mD += i['denom']
    for i in e:
        eN += i['num']
        eD += i['denom']
    for i in s:
        sN += i['num']
        sD += i['denom']
    
    print(mN, eN, sN)
    LCM = lcm(mD, eD, sD)
    fMN = (LCM / mD) * mN
    fEN = (LCM / eD) * eN
    fSN = (LCM / sD) * sN
    fD = fMN + fEN + fSN
    pieArray = [round(fMN/fD* 100),round(fEN/fD *100),round(fSN/fD * 100)]
    return pieArray


#m = [{1:10},{2:10},{1:10}]
#e = [{2:10}, {4:10}, {5:10}]
#s = [{5:10}, {6:10}, {4:10}]
#print(pieGenerator(m, e, s))
