class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_nums=len(nums)
        nums=sorted(nums)
        s= set(nums)
        i=0
        for i in range(total_nums+1):
            if i not in s:
                return i

