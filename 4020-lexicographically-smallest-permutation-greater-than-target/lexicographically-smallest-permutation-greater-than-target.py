class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        for i in range(n - 1, -1, -1):

            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

        
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')
                count[idx] -= 1

                if count[idx] < 0:
                    possible = False
                    break

            if not possible:
                continue

            
            idx = ord(target[i]) - ord('a')

            for j in range(idx + 1, 26):
                if count[j] > 0:

                    count[j] -= 1

                    answer = target[:i]
                    answer += chr(j + ord('a'))

                   
                    for k in range(26):
                        answer += chr(k + ord('a')) * count[k]

                    return answer

        return ""