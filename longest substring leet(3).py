Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,longestSubstring=0,0
        sw=set()
        for r in range(len(s)):
            while s[r] in sw:
                sw.remove(s[l])
                l+=1
            sw.add(s[r])
            longestSubstring=max(longestSubstring,(r-l+1))
        return longestSubstring
         
        