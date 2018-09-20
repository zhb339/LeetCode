int lengthOfLongestSubstring(char* s) {
    
    int max_len = 0, len = 0, start = 0, end = 0;
    int cindex[256] = {0};
    int slen = 0;
    
    slen = strlen(s);

    while (end < slen) {
        if (cindex[s[end]] == 0) {
            cindex[s[end]] = end + 1;
            end++;
            len = end - start;
            if (max_len < len) {
                max_len = len;
            }
            continue;
        } 
        
        
        if (cindex[s[end]] != 0) {
            if (start <= cindex[s[end]] - 1) {
                len = end - start;
                if (max_len < len) {
                    max_len = len;
                }
                start = cindex[s[end]];
                cindex[s[end]] = end + 1;
                end++;
                continue;
            }
                       
            if (start > cindex[s[end]] - 1) {         
                cindex[s[end]] = end + 1;
                end++;
                len = end - start;
                if (max_len < len) {
                    max_len = len;
                }
                continue;
            }
        }
    }

    return max_len;
}