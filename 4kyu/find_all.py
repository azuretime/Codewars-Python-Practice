# Find the number of number of digs digits and the max and min so that sum(digits)=sum_digits

def find_all(s, d):
    xs = [x for x in digs(d) if sum(x) == s]
    if not xs:
        return []
    else:
        reduce_int = lambda xs: int(''.join(map(str, xs)))
        min = reduce_int(xs[0])
        max = reduce_int(xs[-1])    
        return [len(xs), min, max]

def digs(d, start=1):
    """
    >>> list(digs(3, start=9))
    [[9, 9, 9]]
    >>> list(digs(2, start=8))
    [[8, 8], [8, 9], [9, 9]]
    """
    if d == 1:
        for x in range(start, 10):
            yield [x]
    else:
        for x in range(start, 10):
            for y in digs(d - 1, x):
                yield [x] + y
####################################################################

from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]
    
####################################################################

from functools import reduce
def f_all(sum_dig,digs,mid):
    if (digs<=1):
        return([sum_dig>=mid and sum_dig<=9,sum_dig,sum_dig])
    reducesol,presol=lambda a,b:[a[0]+b[0],min(a[1],b[1]),max(a[2],b[2])] if b[0]>0 else a,lambda a,x:[a[0],a[1]+x,a[2]+x]
    ret=reduce(reducesol,[presol(f_all(sum_dig-d,digs-1,d),d*10**(digs-1)) for d in range(mid,min(9,sum_dig-(digs-1)*mid)+1)],[0,10**digs,-1])
    return(ret)
def find_all(sum_dig, digs):
    return((lambda t:t if (t[0]>0) else [])(f_all(sum_dig, digs,1)))
