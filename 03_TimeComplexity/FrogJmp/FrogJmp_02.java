// Score 44% Collectnessは100%だけど、パフォーマンスがダメ　Y-Xが大きいほど長くかかっちゃう
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int X, int Y, int D) {
        // write your code in Java SE 11
        boolean isArrived = false;
        int position = X;
        int count = 0;
        
        if (position == Y) {
            return count;
        } else {
            while (!isArrived) {
                count++;
                position += D;
                if (position >= Y) {
                    isArrived = true;
                    return count;
                }
            }
        }
        return -1;
    }
}