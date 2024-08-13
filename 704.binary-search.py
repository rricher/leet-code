#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
try:
    from typing import List
except Exception as ex:
    print(ex)


class Solution:
    """
    A basic implementation of Binary Search
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        A basic binary search implementation

        Args:
            nums (List[int]): A list of integers in ascending order
            target (int): the target integer

        Returns:
            int: returns the index if found and -1 if not
        """
        start, end = 0, len(nums) - 1
        while end >= start:
            # this can cause overflow with sufficiently large lists
            # middle = (start + end) // 2
            # to fix that instead of adding we subtract each side and add them to start
            middle = start + ((end - start) // 2)
            # if the middle item is larger than the target
            if nums[middle] > target:
                # shift end to the index before middle
                end = middle - 1
            # else if the middle item is smaller
            elif nums[middle] < target:
                # shift start to the index after middle
                start = middle + 1
            # if middle is neither smaller nor larger it must be the target
            else:
                return middle
        return -1


# @lc code=end
