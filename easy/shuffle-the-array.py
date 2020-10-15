# SPECIAL IN PLACE  https://leetcode.com/problems/shuffle-the-array/discuss/675956/In-Place-O(n)-Time-O(1)-Space-With-Explanation-and-Analysis O(n) | O(1)

# https://leetcode.com/problems/shuffle-the-array/

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Examples
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        result = []
        middlePoint = len(nums) // 2
        
        for index in range(len(nums) // 2):
            result.append(nums[index])
            result.append(nums[index + middlePoint])
            
        return result