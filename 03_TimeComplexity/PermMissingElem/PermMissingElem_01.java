// HashMap使う方法　スコア100%
// you can also use imports, for example:
// import java.util.*;
import java.util.HashMap;
import java.util.Map;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 11

        // Mapの定義
        Map<Integer, Integer> cntMap = new HashMap<>();
        for (int i=1; i <= A.length+1; i++) {
            cntMap.put(i, 0); // 各値に対して、count = 0で初期化
        }

        // 要素のカウント
        for (int i=0; i < A.length; i++) {
            cntMap.put(A[i], 1); // 要素があれば、count = 1を入れる
        }

        // 抜け漏れを抽出
        int msElm = -1;
        for (int i=1; i <= A.length+1; i++) {
            if(cntMap.get(i) == 0) {
                msElm = i;
            } 
        }
        return msElm;
    }
}