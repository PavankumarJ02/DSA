class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''if len(nums) == 0:
            return 0
        nums.sort()

        count = 1
        longest = 1 

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+ 1:
                count += 1
            else:
                count =1

            longest = max(longest,count)

        return longest'''
        

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num -1 not in num_set:
                count =1
                while num + count in num_set:
                    count +=1
                longest = max(count,longest)
        return longest
