/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int add_val = 0;
    struct ListNode* lret_head = NULL;
    struct ListNode* cur_node_lret = NULL;

    while (l1 != NULL || l2 != NULL || add_val != 0) {
        if (cur_node_lret == NULL) {
            cur_node_lret = (struct ListNode*)malloc(sizeof(struct ListNode));
            lret_head = cur_node_lret;
        } else {
            cur_node_lret->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            cur_node_lret = cur_node_lret->next;            
        }
        
        memset(cur_node_lret, 0, sizeof(struct ListNode));
        
        if (l1 != NULL) {
            cur_node_lret->val += l1->val;
            l1 = l1->next;
        }

        if (l2 != NULL) {
            cur_node_lret->val += l2->val;
            l2 = l2->next;
        }

        cur_node_lret->val += add_val;
        add_val = cur_node_lret->val / 10;
        cur_node_lret->val = cur_node_lret->val % 10;        
    }

    return lret_head;
}