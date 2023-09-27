class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.length();
        int countOnes = 0;
        for(int i=0; i<n; i++){
            if(s[i] == '1'){
                countOnes++;
            };
        };
        int countZeros = n - countOnes;
        string result = "";
        for(int i=0; i<countOnes-1; i++){
            result.push_back('1');
        };
        for(int i=0; i<countZeros; i++){
            result.push_back('0');
        };
        result.push_back('1');
        return result;
    }
};