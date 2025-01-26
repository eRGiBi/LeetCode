class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> currentSequenceCharacters = new HashSet<>();
        int currentSubLength = 0;
        int longestSubLength = 0;

        if (s.length() == 1) return 1;

        for (int i = 0; i < s.length(); i++) {

            for (int j = i; j < s.length(); j++) {

                if (currentSequenceCharacters.contains(s.charAt(j)) ) {
                    if (longestSubLength < currentSubLength) {
                        longestSubLength = currentSubLength;
                    }
                    currentSubLength = 0;
                    currentSequenceCharacters.clear();
                    break;
                }
                else {
                    currentSequenceCharacters.add(s.charAt(j));
                    currentSubLength++;
                }
            }
        }
        return longestSubLength;
    }
}