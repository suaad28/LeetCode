class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:

                # for each non zero, the index increases linearly
                # hence, at each encounter, it is placed in order
                # automatically replacing the zeros
                
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1

        