from fractions import gcd

def get_lcm(lst):
  return reduce(lambda x, y : x*y/gcd(x,y), lst)

def convertFracts(lst):
  lcm = get_lcm([ y for x, y in lst])
     return [ [x*lcm/y, lcm] for x, y in lst]
     
############################################################################ 

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def convertFracts(lst):
    new_den = lcmm(*[den for num, den in lst])
    return [[num * (new_den / den), new_den] for num, den in lst]     
    
###########################################################################

from fractions import gcd
    
def lcm(a, b):
    return a * b / gcd(a, b)

def convertFracts(lst):
    d = reduce(lcm, [b for a, b in lst])
    return [[a*d/b, d] for a, b in lst]
    
