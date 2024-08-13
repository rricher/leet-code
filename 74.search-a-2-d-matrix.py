#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    """
    A class containing a binary search of a 2D matrix
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Implements a binary search over a 2D matrix

        Args:
            matrix (List[List[int]]): a matrix of sorted ascending integers
            target (int): the target integer

        Returns:
            bool: returns true if found
        """

        start, end = 0, len(matrix) - 1
        while end >= start:
            middle = start + ((end - start) // 2)
            # if the smallest item in the row is larger than the target
            if matrix[middle][0] > target:
                # shift the end pointer to the index before middle
                end = middle - 1
            # else if the largest item is bigger
            elif matrix[middle][-1] < target:
                # shift the start pointer to the index after middle
                start = middle + 1
            else:
                return self.binarySearch(matrix[middle], target)
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        """
        A basic binary search implementation

        Args:
            nums (List[int]): A list of integers in ascending order
            target (int): the target integer

        Returns:
            bool: returns true if found
        """

        start, end = 0, len(nums) - 1
        while end >= start:
            middle = start + ((end - start) // 2)
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                return True
        return False


# @lc code=end
