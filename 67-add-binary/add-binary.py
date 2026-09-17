class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''num_a = int(a,2)
        num_b = int(b,2)
        total = num_a+num_b
        return bin(total)[2:]'''
        tep_a=0
        tep_b=0

        for i in a:
            tep_a =tep_a* 2+int(i)
        for i in b:
            tep_b =tep_b* 2+int(i)
        return bin(tep_a+tep_b)[2:]
        
