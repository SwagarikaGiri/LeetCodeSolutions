class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==1):
            return 1
        else:
            max_=0
            unique=[]
            for i in range(0,len(s)-1):
                unique=[]
                for j in range(i,len(s)):
                    print(s[j])
                    
                    if(s[j] in unique):
                        
                        if(len(unique)>max_):
                            max_ = len(unique)
                            print(unique)
                            print(max_)
                        unique=[]
                    else:
                        unique.append(s[j])
                if(len(unique)> max_):
                    max_ =len(unique)
    
        return max_
                        
