// java版本

public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>() ;
        List<String> tmp = new ArrayList<>();
        helper(0, s.length(), tmp, result, s);
        return result;
    }

    public void helper(int start, int end, List<String> tmp, List<List<String>> result, String string) {
        if (start == end) {
            ArrayList<String> ref = new ArrayList<>(tmp);
            result.add(ref);
            return;
        }

        for (int i = start; i < end; i++) {
            if (!isPalindrome(string.substring(start, i + 1))) {
                continue;
            }
            tmp.add(string.substring(start, i + 1));
            helper(i + 1, end, tmp, result, string);
            tmp.remove(tmp.size() - 1);
        }
    }
    
    public boolean isPalindrome(String string) {
        int start = 0;
        int end = string.length() - 1;
        
        while (start < end) {
            if (string.charAt(start) != string.charAt(end)) {
                return false;
            }
            
            start++;
            end--;
        }
        return true;
    }
}