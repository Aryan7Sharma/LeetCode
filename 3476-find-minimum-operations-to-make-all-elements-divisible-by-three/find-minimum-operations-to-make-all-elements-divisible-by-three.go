package main
import "fmt"
func minimumOperations(nums []int) int {
    answer := 0
    for i := 0 ; i < len(nums) ; i++{
        if(nums[i] % 3 != 0){
            answer++;
        }
    }    
    return answer;
}