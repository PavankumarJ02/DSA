class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_value ={}
        for i in range(len(s)):
            last_value[s[i]]=i
        result=[]
        start =0
        end=0
        for i in range(len(s)):
            
            end = max(end,last_value[s[i]])
            if i == end:
                result.append(i-start +1)
                start=i+1
        return result
        