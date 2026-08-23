class Solution:
    def sumGame(self, num: str) -> bool:
        left_sum =0
        right_sum =0

        left_q = 0
        right_q = 0

        n = len(num)

        for i in range(n//2):
            if num[i]=='?':
                left_q+=1
            else:
                left_sum += int(num[i])

        for i in range(n//2,n):
            if num[i] =='?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        diff = left_sum - right_sum
        q_diff= left_q - right_q

        return 2*(left_sum - right_sum)!=9*(right_q-left_q) 
