class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ind = k-1
        
        l = []
        for x in matrix:
            for y in x:
                l.append(y)
            
        l.sort()
        return(l[ind])
