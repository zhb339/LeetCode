class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < 0):        
            val = -x
        else:
            val = x
            
        val_list = []
        while val:
            val_list.append(val % 10)
            val /= 10
        
        sum = 0
        for v in val_list:
            sum = sum * 10 + v
        
        if (sum > 2415919103):
            sum = 0
            
        if (x < 0x7fffffff and sum > 0x7fffffff):
            sum = 0
            
        if (x > 0x7fffffff and sum < 0x7fffffff):
            sum = 0
            
        if (x < 0):
            sum = -sum
        
        return sum
                