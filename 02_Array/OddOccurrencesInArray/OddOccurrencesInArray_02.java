// 予めソート処理を入れることによって改善した。計算量はO(N) or O(N*log(N))。
// you can also use imports, for example:
// import java.util.*;
import java.util.Arrays;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        
        // 配列のソート
        Arrays.sort(A);
        
        for (int i=0; i < (A.length-1)/2; i++) {
            if(A[2*i] != A[2*i+1]) {
                return A[2*i];
            }
        }
        return A[A.length-1];
    
    }
}