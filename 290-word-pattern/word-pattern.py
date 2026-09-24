class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sentence= s.split()

        pattern_word = {}
        word_pattern ={}

        if len(pattern) != len(sentence):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = sentence[i]

            if char in pattern_word:
                if pattern_word[char] != word:
                    return False
        
            if word in word_pattern:
                if word_pattern[word] != char:
                    return False
        
            pattern_word[char] = word
            word_pattern[word] = char

        return True