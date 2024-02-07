class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        wealth = 0

        for i in accounts:
            for j in i:
                wealth += j
            if wealth > max_wealth:
                max_wealth = wealth
            wealth = 0

        return max_wealth

        return wealth