class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # to store unique characters
        left = 0          # start of the window
        max_len = 0       # to store the result

        for right in range(len(s)):  # right is the end of the window
            while s[right] in char_set:
                char_set.remove(s[left])  # remove the leftmost char to make room
                left += 1

            char_set.add(s[right])        # add the current char to set
            max_len = max(max_len, right - left + 1)  # update result

        return max_len
