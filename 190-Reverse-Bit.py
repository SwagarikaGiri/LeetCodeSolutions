class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)
        binary = binary[2:]
        rev = binary[::-1]
        offset_ =32-len(rev)
        rev = rev + '0'*offset_
        return int(rev,2)


       