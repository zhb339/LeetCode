class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        dic = {}
        mlen = 0
        for i, c in enumerate(s):
            if c in dic:
                if dic[c] >= start and i > start:
                    cur_len = i - start
                    if cur_len > mlen:
                        mlen = cur_len
                    start = dic[c] + 1
            dic[c] = i
       
        if len(s) - start > mlen:
            mlen = len(s) - start
            
        return mlen
