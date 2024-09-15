#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int bitwiseAnd(int N, int K) {
    int max_value = 0;
    
    // Iterate through all pairs A < B
    for (int A = 1; A < N; A++) {
        for (int B = A + 1; B <= N; B++) {
            int result = A & B;
            
            // Check if result is less than K and greater than max_value found so far
            if (result < K && result > max_value) {
                max_value = result;
            }
            
            // Early exit if we already reach the maximum possible value
            if (max_value == K - 1) {
                return max_value;
            }
        }
    }
    
    return max_value;
}

int main() {
    int T;
    scanf("%d", &T);  // Number of test cases
    
    for (int i = 0; i < T; i++) {
        int N, K;
        scanf("%d %d", &N, &K);  // Read N and K for each test case
        
        // Compute the result and print it
        printf("%d\n", bitwiseAnd(N, K));
    }
    
    return 0;
}
