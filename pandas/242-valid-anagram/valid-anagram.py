class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #a sorted string would be equal 
        
        if sorted(s) == sorted(t):
            return True
        else:
            return False