class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start,end = 0,len(letters)-1
        
        while start+1 < end:
            mid = start + (end-start)//2
            if letters[mid]>target:
                end = mid
            elif letters[mid]<target:
                start = mid
            else:
                start = mid
        
        if(letters[start]>target):
            return letters[start]
        
        if(letters[end]>target):
            return letters[end]
        
        return letters[0]