class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]

        def backtrack(path,remaining):
            if len(remaining)==0:
                result.append(path)
                return
            
            for i in range(len(remaining)):
                num = remaining[i]

                new_path = path + [num]
                new_remaining = remaining[:i]+ remaining[i+1:]

                backtrack(new_path,new_remaining)
        backtrack([],nums)

        return result