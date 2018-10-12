# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            if l2 is None:
                return None
            else:
                return l2
        else:
            if l2 is None:
                return l1
        
        sum = l1.val + l2.val
        ca = sum / 10
        re = sum % 10
        head_node = ListNode(re)
        cnode = head_node
        
        while True:
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                sum = l1.val + l2.val + ca
                ca = sum / 10
                re = sum % 10
                nnode = ListNode(re)
                cnode.next = nnode
                cnode = nnode
            elif l1.next is None:
                if l2.next is None:
                    if ca is 0:
                        return head_node
                    else:
                        nnode = ListNode(ca)
                        cnode.next = nnode
                        return head_node
                else:
                    while l2.next:
                        l2 = l2.next
                        sum = l2.val + ca
                        ca = sum / 10
                        re = sum % 10
                        nnode = ListNode(re)
                        cnode.next = nnode
                        cnode = nnode
                    if ca:
                        nnode = ListNode(ca)
                        cnode.next = nnode
                    return head_node
            elif l2.next is None:
                if l1.next is None:
                    if ca is 0:
                        return head_node
                    else:
                        nnode = ListNode(ca)
                        cnode.next = nnode
                        return head_node
                else:
                    while l1.next:
                        l1 = l1.next
                        sum = l1.val + ca
                        ca = sum / 10
                        re = sum % 10
                        nnode = ListNode(re)
                        cnode.next = nnode
                        cnode = nnode
                    if ca:
                        nnode = ListNode(ca)
                        cnode.next = nnode
                    return head_node
        