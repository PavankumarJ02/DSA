class Solution:
    def reverseWords(self, s: str) -> str:
        run = s.split()
        run.reverse()

        return " ".join(run)
        