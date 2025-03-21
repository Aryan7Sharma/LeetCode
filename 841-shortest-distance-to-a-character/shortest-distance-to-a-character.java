import java.util.ArrayList;

class Solution {
    public int[] shortestToChar(String s, char c) {
        int[] arr1 = new int[s.length()];  // Corrected array initialization
        ArrayList<Integer> cindx = new ArrayList<>(); // Store indexes of character 'c'
        
        // First pass: Find all indexes of character 'c'
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) { // Corrected string indexing
                cindx.add(i);
            }
        }
        
        // Second pass: Compute shortest distance for each character
        for (int i = 0; i < s.length(); i++) {
            int mdist = s.length();
            for (int j = 0; j < cindx.size(); j++) {
                if(Math.abs(i-cindx.get(j))<mdist){
                    mdist=Math.abs(i-cindx.get(j));
                }
            }
            arr1[i] = mdist; // Store in array
        }
        
        return arr1; // Return the final array
    }
}
