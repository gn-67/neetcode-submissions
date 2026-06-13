class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */

    //since every element is exactly 1 greater than the previous element
    //our starting values will have no value - 1 in nums
    //so we can start from those then increment up, keeping track of the length and then getting the max between the current length and the max length
    //so we only check the starting values
    // i think we can use a set since we do not care about duplicates and can easily lookup values with O(1) time
    longestConsecutive(nums) {
        let setNums = new Set(nums)
        let maxLen = 0

        for (let num of setNums){
            let len = 1
            let cur = num
            if (setNums.has(cur - 1)){
                continue
            }
            else{
                while (setNums.has(cur + 1)){
                    len += 1
                    cur += 1
                }
            }
            maxLen = Math.max(maxLen, len)
        }

        return maxLen
    }
}
