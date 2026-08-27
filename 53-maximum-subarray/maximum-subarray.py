class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximium = nums[0]

        for i in nums[1:]:
            current = max(i,current+i)
            maximium = max(maximium,current)

        return maximium

