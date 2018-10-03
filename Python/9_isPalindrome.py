class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        
        val = x
        val_list = []
        while val:
            val_list.append(val % 10)
            val = val / 10
        sum = 0    
        for v in val_list:
            sum = sum * 10 + v
        
        if (sum == x):
            return True
        
        return False
        