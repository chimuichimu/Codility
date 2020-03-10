// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N) {
        // write your code in Java SE 11
        
        // Convert to Binary
        String bin = Integer.toBinaryString(N);

        // Gap Length
        int len_max = 0;
        int len_temp = 0;

        // Count
        for (int i=1; i < bin.length(); i++){
            if(bin.charAt(i) == '1' ){
                if(len_temp > len_max){
                    len_max = len_temp;
                }
                len_temp = 0;
            } else{ 
                len_temp += 1;
            }
        }
        return len_max;
    }
}