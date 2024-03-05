class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        for i in range(1,len(s)):
            s_left = s[:i]
            s_right = s[i:]
            if len(set(s_left)) ==  len(set(s_right)):
                count+=1
        return count
