// スコア100% 左側の合計値、右側の合計値、左側と右側の差分をループ処理の中で更新する。
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 11
        int leftSum = 0;
        int rightSum = 0;
        for (int i=0; i < A.length; i++) {
            rightSum += A[i];
        }
        int minDif = Integer.MAX_VALUE;
        
        for (int i=1; i < A.length; i++) {
            leftSum += A[i-1];
            rightSum -= A[i-1];
            minDif = Math.min(minDif, Math.abs(rightSum-leftSum));
        }
        
        return minDif;
    }
}