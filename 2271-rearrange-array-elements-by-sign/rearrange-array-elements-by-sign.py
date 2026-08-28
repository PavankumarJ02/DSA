class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postivi = []
        negativi = []
        for num in nums:
            if  num >0:
                postivi.append(num)
            else:
                negativi.append(num)
        ans=[]
        for i in range(len(postivi)):
            ans.append(postivi[i])
            ans.append(negativi[i])
        return ans
