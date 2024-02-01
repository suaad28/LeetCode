class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
 
        increasing = True
        decreasing = True

        for j in range(1,len(nums)):
            if nums[j] > nums[j - 1]:
                decreasing = False
            elif nums[j] < nums[j - 1]:
                increasing = False

        return increasing or decreasing


        # # monotone increasing
        # if nums[i+1]-nums[i] > 0:
        #     for j in range(1,len(nums)-1):
        #         if nums[j+1] - nums[j] < 0:  #if we encounter negative
        #             return False

        # # monotone decreasing
        # else:
        #     for j in range(1,len(nums)-1):
        #         if nums[j+1] - nums[j] > 0: #if we encounter positive
        #             return False
        
        # return True
