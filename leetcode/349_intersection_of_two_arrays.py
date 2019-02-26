class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n = len(nums1),len(nums2)
        res = []
        if m <= n:
            for e in nums1:
                if e in nums2 and e not in res:
                    res.append(e)
        else:
            for e in nums2:
                if e in nums1 and e not in res:
                    res.append(e)
        return res