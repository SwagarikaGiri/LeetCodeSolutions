class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for ele in nums:
            if ele in count:
                count[ele]= count[ele]+1
            else:
                count[ele]=1
        for key,values in count.items():
            if values > (len(nums)/2):
                return key

        return 0