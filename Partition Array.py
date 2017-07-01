"""
Given an array "nums" of integers and an int "k", Partition the array (i.e move the elements in "nums") such that,

    * All elements < k are moved to the left

    * All elements >= k are moved to the right

Return the partitioning Index, i.e the first index "i" nums[i] >= k.

Note
You should do really partition in array "nums" instead of just counting the numbers of integers smaller than k.

If all elements in "nums" are smaller than k, then return "nums.length"

Example
If nums=[3,2,2,1] and k=2, a valid answer is 1.

Challenge
Can you partition the array in-place and in O(n)?
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
            return 0
        pr = len(nums)-1
        i = 0
        while i <= pr:
            while i <= pr and nums[i] < k:
                i+=1
            while i <= pr and nums[pr]>=k:
                pr-=1
            if i <= pr:
                nums[i], nums[pr] = nums[pr], nums[i]
                i+=1
                pr-=1
        return i
                
