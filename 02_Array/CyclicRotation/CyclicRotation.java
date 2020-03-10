// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int[] solution(int[] A, int K) {
        // write your code in Java SE 11

        int[] newA = new int[A.length];

        if (K == 0){
            return A;
        } else {
            for (int i = 1; i <= K; i++) {
                for (int j = 0; j < A.length; j++) {
                    if (j == 0) {
                        newA[j] = A[A.length-1];
                    } else {
                        newA[j] = A[j-1];
                    }
                }
                
                for (int k = 0; k < A.length; k++) {
                    A[k] = newA[k];
                }
                
            }
            return newA;
        }
    }
}