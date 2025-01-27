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

class Solution2 {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> currentSequenceCharacters = new HashSet<>();
        int longestSubLength = 0;
        int left = 0;

        if (s.length() == 1) return 1;

        for (int right = 0; right < s.length(); right++) {

            if (currentSequenceCharacters.contains(s.charAt(right)) ) {

                do {
                    currentSequenceCharacters.remove(s.charAt(left));
                    left++;

                } while (currentSequenceCharacters.contains(s.charAt(right)));

                currentSequenceCharacters.add(s.charAt(right));

            }
            else {
                currentSequenceCharacters.add(s.charAt(right));
                longestSubLength = Math.max(longestSubLength, right - left + 1);
            }
        }
        return longestSubLength;
    }
}

class Solution3 {
    public int lengthOfLongestSubstring(String s) {

        int n = s.length();
        int longestSubLength = 0;

        int[] charIndex = new int[128];
        Arrays.fill(charIndex, -1);

        int left = 0;

        for (int right = 0; right < n; right++) {
            if (charIndex[s.charAt(right)] >= left) {
                left = charIndex[s.charAt(right)] + 1;
            }
            charIndex[s.charAt(right)] = right;
            longestSubLength = Math.max(longestSubLength, right - left + 1);
        }

        return longestSubLength;
    }
}