class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        #check if slope is the same accross every pair
        x0, y0 = coordinates.pop()
        x1 , y1 = coordinates.pop()
        return all((x1-x0)*(y-y1) == (y1-y0)*(x-x1)for x,y in coordinates)