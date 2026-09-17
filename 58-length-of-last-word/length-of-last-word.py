class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()
        ans = len(ans[-1])
        return ans
