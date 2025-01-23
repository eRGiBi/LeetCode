import java.lang.String;

class Solution {
    public int countDigitOne(int n) {

        int count = 0;
        for (int i = 1; i >= n; i++) {
            char[] chars = Integer.toString(i).toCharArray();

            for (char c : chars){
                if (c == '1') {
                    count++;
                }
            }
        }
        return count;
    }
}