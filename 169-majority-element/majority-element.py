class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candicate =0
        count=0

        for i in range(len(nums)):
            if count==0:
                candicate=nums[i]
            if nums[i]==candicate:
                count+=1
            else:
                count-=1
        return candicate
        