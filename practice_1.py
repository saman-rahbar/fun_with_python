#! \usr\bin\env\ python3

"""
Question_1:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
 
#Solution_Question_1:

class Solution:
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                raise ValueError("The value wan't found!")
            else:
                print [h[n], i]


test_1  = Solution()
test_1.twoSum([1, 2, 10, 42], 43)






 
