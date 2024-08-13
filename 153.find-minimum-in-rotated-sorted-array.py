#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    """
    Find the minimum in rotated sorted array
    """

    ### my solution ###
    def findMin(self, nums: List[int]) -> int:
        """
        find minimum

        Find the minimum in a sorted array that has been rotated n number of times

        Args:
            nums (List[int]): a list of sorted rotated integers

        Returns:
            int: the minimum in the array
        """

        middle, start, end = 0, 0, len(nums) - 1
        while start < end:
            # set middle
            middle = start + ((end - start) // 2)
            # if middle is bigger then end
            if nums[middle] > nums[end]:
                # Shift the start to middle + 1 since we know that middle is part of the rotation
                start = middle + 1
                # set middle to start incase there is only 1 iteration of while so we can return the correct number
                middle = start
            # if middle is smaller than start
            elif nums[middle] < nums[start]:
                # shift the end bound to the middle
                # this will allow the previous condition to trigger next loop since we dont know how far rotated start is
                end = middle
            # if middle is smaller than end
            elif nums[middle] < nums[end]:
                # we know that middle is larger than start as we need to narrow the search
                end = middle
        return nums[middle]

    ### NeetCode's Solution ###
    def findMinNeetCode(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = start + (end - start) // 2
            curr_min = min(curr_min, nums[mid])

            # right has the min
            if nums[mid] > nums[end]:
                start = mid + 1

            # left has the  min
            else:
                end = mid - 1

        return min(curr_min, nums[start])


# @lc code=end
