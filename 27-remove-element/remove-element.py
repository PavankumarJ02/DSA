class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ans = []

        for number in nums:
            if number != val:
                ans.append(number)

        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)
            