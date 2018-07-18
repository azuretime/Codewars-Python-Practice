def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        #if the peak is a plateau, it should only return the position of the first element of the plateau    
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
    
    
    
    Test.it('should support finding peaks')
Test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})

Test.it('should support finding peaks, but should ignore peaks on the edge of the array')
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})

Test.it('should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})

Test.it('should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})

Test.it('should support finding peaks, but should ignore peaks on the edge of the array')
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
  
Test.it('should support finding peaks, but should ignore peaks on the edge of the array')
Test.assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
  
Test.it('should support finding peaks, despite the plateau')
Test.assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})

Test.it('should support finding peaks')
Test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})

Test.it('should return an object with empty arrays if the input is an empty array')
Test.assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})

Test.it('should return an object with empty arrays if the input does not contain any peak')
Test.assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})

Test.describe("Random tests")
from random import randint
def sol_peaks(arr):
    res={"pos":[], "peaks":[]}
    for i in xrange(1, len(arr)-1):
        if arr[i-1]<arr[i]:
            temp=i
            while arr[i]==arr[i+1] and i<len(arr)-2: i+=1
            if arr[i]>arr[i+1]:
                res["pos"]+=[temp]
                res["peaks"]+=[arr[temp]]
            i+=1
        else: i+=1
    return res

for _ in xrange(40):
    arr=[randint(-5,20) for x in xrange(randint(5,30))]
    Test.it("Testing for %s" %arr)
    Test.assert_equals(pick_peaks(arr),sol_peaks(arr),"It should work for random inputs too")
