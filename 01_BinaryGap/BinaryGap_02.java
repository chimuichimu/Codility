// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N) {
        // write your code in Java SE 11
        
        // Convert to Binary
        String bin = Integer.toBinaryString(N);
        
        // Split by 1
        String[] zeros = bin.split("1", 0);
        int index = zeros.length;
        
        // 1000, 10000などはカウントしないようにする
        if (N % 2 == 0){
            index -= 1;
        }
        
        // Decide Max
        int max = 0;
        for (int i =0; i < index; i++){
            if (zeros[i].length() > max ){
                max = zeros[i].length();
            }
        }
        
        return max;
    }
}