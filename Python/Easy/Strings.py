#   Reverse Integer
def reverse(self, x: int) -> int:
    if x > 0:
        x = int(str(x)[::-1])
    else:
        x = int(str(abs(x))[::-1]) * -1
    
    if x < -2**31 or x > 2**31 -1:
        x = 0
    
    return x

#   First Unique Character in a String
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
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) == len(t) and sorted(s) == sorted(t):
        return True
    return False

#     String to Integer (atoi)
def myAtoi(self, s: str) -> int:
    op = ""
    s = s.lstrip()
    
    #checking empty string and starting characters
    if s == "" or s[0].isalpha() or s[0] == ".":
        print("RETURN 1")
        return 0
    
    sign = 1
    i = 0
    
    # Handle sign
    if s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        i += 1
    
    # Parse digits
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    
    num *= sign

    # handle max and min values     
    if num > 2**31 -1:
        print("RETURN 6")
        return 2**31-1
    
    if num < -2**31:
        print("RETURN 7")
        return -2**31
    
    return num

#  Implement strStr()
def strStr(self, haystack: str, needle: str) -> int:
        r = -1
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                print(str(haystack[i:i+len(needle)]), needle)
                if haystack[i:i+len(needle)] == needle:
                    r = i
                    break
        return r

# Longest Common Prefix
def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        prfx = strs[0]

        if (len(strs)==1):
            return strs[0]
        for i in range(len(strs)):
            while not strs[i].startswith(prfx):
                prfx = prfx[:-1]
                if not prfx:
                    return ""
        return prfx