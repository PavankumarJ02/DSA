class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s ={}
        map_t ={}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in map_s and map_s[a] != b:
                return False
            if b in map_t and map_t[b] != a:
                return False

            map_s[a] = b
            map_t[b] = a
        return True