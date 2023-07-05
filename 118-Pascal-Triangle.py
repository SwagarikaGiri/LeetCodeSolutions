class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in range(1,numRows+1):
            if i == 1:
                pascal.append([1])
            elif i == 2:
                pascal.append([1,1])
            else:
                last = pascal[-1]
                next_ = [1]
                for j in range(0,len(last)-1):
                    next_.append(last[j]+last[j+1])
                next_.append(1)
                pascal.append(next_)
        return pascal
        
                    
                   
                
