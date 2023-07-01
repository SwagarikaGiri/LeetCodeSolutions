class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        nums.sort()
        print(nums)
        unique = None
        for i in range(0,len(nums)-1):
            if(nums[i] !=unique):
                unique = nums[i]
                if(nums[i]!=nums[i+1]):
                    return nums[i]
        return nums[-1]