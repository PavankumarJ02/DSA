class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        if length_s == length_t :
            return sorted(s)==sorted(t)
        else:
            return False