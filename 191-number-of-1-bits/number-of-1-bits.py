class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        '''countlist =[int(x) for x in binary] '''
        totalcount=0
       

        for i in binary:
            if i == "1":
                totalcount+=1
            

        return totalcount

        
        