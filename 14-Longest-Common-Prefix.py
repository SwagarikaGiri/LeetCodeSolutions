class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        element1=strs[0]
        for end in range(len(element1),0,-1):
            sub=element1[0:end]
            print(sub)
            count=0
            for i in range(1,len(strs)):
                if(strs[i].startswith(sub)):
                    count=count+1
                else:
                    break
            if(count==len(strs)-1):
                return sub
        return ""