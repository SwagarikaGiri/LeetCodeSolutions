class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        #create a dictionary
        alpha_dict ={
            'A':1,
            'B':2,
            'C':3,
            'D':4,
            'E':5,
            'F':6,
            'G':7,
            'H':8,
            'I':9,
            'J':10,
            'K':11,
            'L':12,
            'M':13,
            'N':14,
            'O':15,
            'P':16,
            'Q':17,
            'R':18,
            'S':19,
            'T':20,
            'U':21,
            'V':22,
            'W':23,
            'X':24,
            'Y':25,
            'Z':26 }
        columnTitleRev = columnTitle[::-1]
        power_ =0
        sum_ =0
        for i in range(0,len(columnTitleRev)):
                val = alpha_dict[columnTitleRev[i]]
                sum_ = sum_ + pow(26,power_)*val
                power_ = power_ + 1
        return sum_




           