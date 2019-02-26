class Solution:
    # 64 ms 12.9 MB
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n = len(nums1),len(nums2)
        res = []
        if m <= n:
            for e in nums1:
                if e in nums2:
                    nums2.remove(e)
                    res.append(e)
        else:
            for e in nums2:
                if e in nums1:
                    nums1.remove(e)
                    res.append(e)
        return res

    # 44 ms 13.2 MB, 用双指针好像更快一点
    def intersect2(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        pt1 = pt2 = 0
        res = []

        while pt1<len(nums1) and pt2<len(nums2):
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
        return res

    # use Counter 44 ms 13.4 MB
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1
        return res