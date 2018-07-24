#https://www.codewars.com/kata/next-smaller-number-with-the-same-digits

def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))
################################################    

def greedy(n):
    lst = [0]*10
    for digit in n:
        lst[int(digit)]+=1

    for i in range(int(n[0])-1, -1, -1):
        if lst[i]>0:
            lst[i]-=1
            out=str(i)
            break
    else:
        return -1

    for i in range(9,-1,-1):
        out+=str(i)*lst[i]
    return out

def next_smaller(n):
    n=str(n)
    for idx in range(len(n)-1,0,-1):
        poss = greedy(n[idx:])
        if poss==-1:
            continue
        if int(poss)<int(n[idx:]):
            return int(n[:idx] + poss)
    poss=greedy(n)
    if poss==-1 or poss[0]=='0':
        return -1
    return int(poss)
    
#--------Time out---------------------------------------------
def next_smaller(n):
    if n <=20: return -1       
    l = [ int(i) for i in str(n)]
    if l.count(l[0]) == len(l): return -1 

    from itertools import permutations

    perm = list(permutations(l))
    for i in range(len(perm)):
        perm[i] = int(''.join(str(v) for v in perm[i]))
    perm.sort(reverse = True)
    for j in perm:
        if j<n:
            return j
    return -1  
    
###########################################################
def next_smaller(n):
    if n <=20: return -1       
    l = [ int(i) for i in str(n)]
    if l.count(l[0]) == len(l): return -1 
    
    import collections

    c = collections.Counter(l)
    c1 = dict(c)
    s = l.copy()
    s.sort()
    if s[0] == 0:
        for a in range(1,len(s)):
            if s[a]!= 0:
                s[0] = s[a]
                s[a] = 0
                break
                
    sn = int(''.join(str(v) for v in s))  
    print(sn)
    for i in range(n-1,sn-1,-1):
        c2 = collections.Counter([int(x) for x in str(i)])
        if dict(c2)==c1:
            return i
    
  #wrong
def next_smaller(n):
    if n <=20: return -1       
    l = [ int(i) for i in str(n)]
    if l.count(l[0]) == len(l): return -1 
    
    print(l)
    for j in range(len(l)-2,-1,-1):
        ls = l.copy()
        ls[j]=l[j+1]
        ls[j+1]=l[j]
        ret = int(''.join(str(v) for v in ls))
        print(ls[0]!=0,ret<n,ret,n)
        if ls[0]!=0 and ret<n:
            return ret
    return -1   
