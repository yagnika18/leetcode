class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = ' '.join(word[::-1] for word in s.split())
        return reversed_words
        