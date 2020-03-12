// スコア100% ジャンプしてちょうど着くときの場合分けが必要だった
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int X, int Y, int D) {
        // write your code in Java SE 11
        if (X == Y) {
            return 0;
        } else if ((Y - X) % D == 0){
            return (Y - X) / D;
        } else {
            return (Y - X) / D + 1;
        } 
    }
}