class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        s = sorted(salary)
        return (sum(s[1:len(s)-1]))/(len(s)-2)
