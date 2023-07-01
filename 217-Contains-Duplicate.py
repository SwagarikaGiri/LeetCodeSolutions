class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        len_unique = len(set(nums))
        if(len_nums == len_unique):
            return False
        else:
            return True