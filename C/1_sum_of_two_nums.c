/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int index1, index2;
    int *ret;

    ret = malloc(2 * sizeof(int));
    memset(ret, 0, 2 * sizeof(int));
    
    for (index1 = 0; index1 < numsSize - 1; index1++) {
        for (index2 = index1 + 1; index2 < numsSize; index2++) {
            if (nums[index1] + nums[index2] == target) {
                ret[0] = index1;
                ret[1] = index2;
                return ret;
            }
        }
    }

    return ret;
}