class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = len(numbers)
        i,j = 0,m-1
        while (i<j):
            a = numbers[i]
            b = target - a
            if numbers[j]<b:
                i += 1
            elif numbers[j]>b:
                j += -1
            else:
                return list((i+1,j+1))
        return -1