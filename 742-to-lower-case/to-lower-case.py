class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(0,len(s)):
            if s[i].isupper():
                #Strings are immutable. Hence need to recreate the string
                s = s[:i] + s[i].lower() + s[i+1:]
        return s
            