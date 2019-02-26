class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums)-1
        
        while start+1 < end:
            mid = start + (end-start)//2
            if nums[mid]>target:
                end = mid
            elif nums[mid]<target:
                start = mid
            else:
                return mid
        
        if(nums[start]==target):
            return start
        if(nums[end]==target):
            return end
        
        return -1