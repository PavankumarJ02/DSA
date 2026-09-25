class Solution:
    def minTimeToType(self, word: str) -> int:
        cu='a'
        t=0
        for c in word:
            diff=abs(ord(c)-ord(cu))
            t+=min(diff,26-diff)+1
            cu=c
        return t