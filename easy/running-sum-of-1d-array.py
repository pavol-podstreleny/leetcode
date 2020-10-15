# https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

#Examples:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


# O(N) time | O(1) space
class Solution:
    def runningSumMy(self, nums: List[int]) -> List[int]:
        
        runningSum = 0
        
        for index, number in enumerate(nums):
            actualNumber = nums[index]
            nums[index] = actualNumber + runningSum
            runningSum += actualNumber
        
        return nums

    
