class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            val1 = nums[i]
            val2 = target - val1
            try:
                id_ = nums.index(val2)
                if(i!=id_):
                    return[i,id_]
            except:
                pass