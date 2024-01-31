class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cs = {}
        ct = {}
        
        for char in s:
            cs[char] = cs.get(char, 0) + 1  
        
        for char in t:
            ct[char] = ct.get(char, 0) + 1

        for char, count in ct.items():  #iterate through the longer string
            if cs.get(char, 0) != count:
                return char