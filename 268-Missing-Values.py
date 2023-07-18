class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        last_num = nums[-1]
        if(length != last_num+1):
            extended_list = [ele for ele in range(last_num+1)]
            extended_set = set(extended_list)
            nums_set = set(nums)
            missing_value = extended_set - nums_set
            print(missing_value)
            return list(missing_value)[0]
        else:
            return length