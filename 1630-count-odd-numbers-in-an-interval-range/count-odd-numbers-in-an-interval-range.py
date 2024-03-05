class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        if low%2!=0 or high%2!=0:
            count = ((high-low)/2) + 1
        else:
            count = (high-low)/2
        return count
