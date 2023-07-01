class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string_ = re.sub(r'[^a-zA-Z0-9]', '', s)
        string_ = string_.lower()
        rev_string_ = string_[::-1]
        print(string_)
        print(rev_string_)
        if(string_ == rev_string_):
            return True
        else:
            return False