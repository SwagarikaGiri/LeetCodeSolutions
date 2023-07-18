class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(str(s))
        t = list(str(t))
        s.sort()
        t.sort()
        if(len(s)!=len(t)):
            return False
        for i in range(0,len(s)):
            if s[i]!=t[i]:
                return False
        return True  
      