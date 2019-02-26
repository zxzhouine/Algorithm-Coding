class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start,end = 0,len(A)-1
        
        while start + 1 < end:
            mid = start + (end-start)//2
            if A[mid]>A[mid-1]:
                if A[mid]>A[mid+1]:
                    return mid
                else:
                    start = mid
            else:
                end = mid
        
        if A[start]>A[start-1] and A[start]<A[start+1]:
            return start
        if A[end]>A[end-1] and A[end]<A[end+1]:
            return end