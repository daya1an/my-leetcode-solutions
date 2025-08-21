#   Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(abs(x))[::-1]) * -1
        
        if x < -2**31 or x > 2**31 -1:
            x = 0
        
        return x

#   First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        op = -1
        for i in range(len(s)):
            if s[i] in cnt:
                cnt[s[i]] +=1
            else:
                cnt[s[i]] = 1
        
        for e in cnt:
            if int(cnt[e]) == 1:
                return s.index(e)
        
        return -1

#   Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and sorted(s) == sorted(t):
            return True
        return False
