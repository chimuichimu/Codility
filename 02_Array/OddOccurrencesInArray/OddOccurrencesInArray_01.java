// よくなかったやつ。計算量がO(N^2)。
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 11
        boolean hasPair = false;
        
        for (int i=0; i<A.length; i++) {
            for (int j=0; j<A.length; j++) {
                if (i != j){
                    if (A[i] == A[j]) {
                        hasPair = true;
                    }
                }
            }
            if (!hasPair) {
                return A[i];
            }
            hasPair = false;
        }
        return -1;
    }
}