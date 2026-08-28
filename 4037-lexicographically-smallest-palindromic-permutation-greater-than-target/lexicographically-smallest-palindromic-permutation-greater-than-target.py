class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

       
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

    
        calendrix = (s, target)

        
        odd = 0
        middle = -1

        for i in range(26):
            if freq[i] % 2 == 1:
                odd += 1
                middle = i

        if odd > 1:
            return ""

       
        for i in range(26):
            freq[i] //= 2

        half = n // 2
        ans = list(target)

       
        pos = 0

        while pos < half:
            idx = ord(target[pos]) - ord('a')

            if freq[idx] == 0:
                break

            ans[pos] = target[pos]
            freq[idx] -= 1
            pos += 1

       
        def make_palindrome():
            if middle != -1:
                ans[half] = chr(middle + ord('a'))

            for i in range(half):
                ans[n - 1 - i] = ans[i]

    
        if pos == half:
            make_palindrome()

            result = ''.join(ans)

            if result > target:
                return result

      
        while True:

            if pos < half:
                idx = ord(target[pos]) - ord('a')

               
                for j in range(idx + 1, 26):

                    if freq[j] > 0:
                        ans[pos] = chr(j + ord('a'))
                        freq[j] -= 1

                     
                        next_pos = pos + 1

                        for k in range(26):
                            for _ in range(freq[k]):
                                ans[next_pos] = chr(k + ord('a'))
                                next_pos += 1

                        make_palindrome()

                        return ''.join(ans)

            
            if pos == 0:
                return ""

            pos -= 1

            
            idx = ord(target[pos]) - ord('a')
            freq[idx] += 1