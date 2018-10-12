class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 <= l2:
            m = nums1
            lm = l1
            n = nums2
            ln = l2
        else:
            m = nums2
            lm = l2
            n = nums1
            ln = l1
        
        if lm is 0 and ln is not 0:
            if ln % 2 is 0:
                return (n[int(ln / 2)] + n[int(ln / 2 - 1)]) / 2.0
            else:
                return n[(ln - 1) / 2]
        elif lm is 0 and ln is 0:
            return None
        
        if m[lm - 1] <= n[0]:
            if (lm + ln) % 2 is 0:
                if lm == ln:
                    return (m[lm - 1] + n[0]) / 2.0
                else:
                    return (n[(lm + ln) / 2 - lm] + n[(lm + ln) / 2 - 1 - lm]) / 2.0
            else:
                return n[(lm + ln - 1) / 2 - lm]
        elif m[0] >= n[ln - 1]:
            if (lm + ln) % 2 is 0:
                if lm == ln:
                    return (m[0] + n[ln - 1]) / 2.0
                else:
                    return (n[(lm + ln) / 2] + n[(lm + ln) / 2 - 1]) / 2.0
            else:
                return n[(lm + ln - 1) / 2]
        
        if (lm + ln) % 2 == 0:
            if m[lm - 1] <= n[(ln - lm) / 2]:
                return (max(m[lm - 1], n[(ln - lm) / 2 - 1]) + n[(ln - lm) / 2]) / 2.0
            elif m[0] >= n[(ln + lm) / 2 - 1]:
                #return n[(ln - lm) / 2 - 1]
                return (min(m[0], n[(ln + lm) / 2]) + n[(ln + lm) / 2 - 1]) / 2.0
                
            maxi = lm
            mini = 0
            while True:
                i = int((maxi + mini) / 2)
                j = (lm + ln) / 2 - 1 - i
                if j != ln - 1 and m[i] > n[j + 1]:
                    maxi = i
                else:
                    if i != lm - 1 and m[i + 1] < n[j]:
                        mini = i
                    else:
                        if i > 0 and m[i - 1] >= n[j]:
                            return (m[i] + m[i - 1]) / 2.0
                        elif j > 0 and m[i] < n[j - 1]:
                            return (n[j] + n[j - 1]) / 2.0
                        else:
                            return (m[i] + n[j]) / 2.0
                i = int((maxi + mini) / 2)
        elif (lm + ln) % 2 != 0:
            if m[lm - 1] <= n[(ln - lm + 1) / 2]:
                return max(m[lm - 1], n[(ln - lm + 1) / 2 - 1])
            elif m[0] >= n[(lm + ln - 1) / 2 - 1]:
                return min(m[0], n[(lm + ln - 1) / 2])
            
            maxi = lm
            mini = 0
            while True:
                i = int((maxi + mini) / 2)
                j = (lm + ln + 1) / 2 - 2 - i
                if j != ln - 1 and m[i] > n[j + 1]:
                    maxi = i
                else:
                    if i != lm - 1 and m[i + 1] < n[j]:
                        mini = i
                    else:
                        return max(m[i], n[j])
                i = int((maxi + mini) / 2)