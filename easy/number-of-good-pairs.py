# https://leetcode.com/problems/number-of-good-pairs/

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

 
##########
# Examples
##########

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.


# O(N) time | O(N) space
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        goodPairs = 0
        
        numberHistogram = dict()
        
        for number in nums:
            if number in numberHistogram:
                goodPairs += numberHistogram[number]
                numberHistogram[number] += 1
            else:
                numberHistogram[number] = 1
        
        return goodPairs

