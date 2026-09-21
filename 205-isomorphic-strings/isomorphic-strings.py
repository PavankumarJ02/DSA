class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_pattern = []
        t_pattern = []

        s_seen = {}
        t_seen = {}

        for i in range(len(s)):

            if s[i] not in s_seen:
                s_seen[s[i]] = len(s_seen)

            if t[i] not in t_seen:
                t_seen[t[i]] = len(t_seen)

            s_pattern.append(s_seen[s[i]])
            t_pattern.append(t_seen[t[i]])

        return s_pattern == t_pattern