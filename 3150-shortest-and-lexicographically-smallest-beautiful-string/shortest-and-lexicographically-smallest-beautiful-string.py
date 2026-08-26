class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        one=[]
        for i in range(len(s)):
            if s[i]=='1':
                one.append(i)
        if len(one) <k :
            return ""
        ans = s[one[0]:one[k-1]+1]

        for i in  range(1,len(one) - k +1):
            start = one[i]
            end = one[i+k-1]

            current = s[start:end +1]

            if len(current) <len(ans):
                ans = current
            elif len(current) == len(ans) and current <ans:
                ans = current
        return ans
        