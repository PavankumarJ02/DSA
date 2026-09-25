class Solution:
    def minTimeToType(self, word: str) -> int:

        current = 0
        total = 0

        for char in word:

            target = ord(char) - ord('a')

            distance = abs(current - target)

            distance = min(distance, 26 - distance)

            total += distance + 1

            current = target

        return total