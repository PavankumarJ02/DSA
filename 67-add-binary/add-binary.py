class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        tep_a=0
        tep_b=0

        for i in a:
            tep_a =tep_a* 2+int(i)
        for i in b:
            tep_b =tep_b* 2+int(i)
        return bin(tep_a+tep_b)[2:]
        
