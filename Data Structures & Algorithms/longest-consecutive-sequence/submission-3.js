class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        //first we sort the array, add it to a set
        //we iterate through the array, only looking at values where value - 1 doesn't exist (no prev)
        //then we iterate forward, until we reach a value that is greater than + 1
        //we store the length of the result compare it with the current max value, if its greater then we update max
        // return max length
        let maxlen = 0
        nums = new Set(nums.sort())

        for (const value of nums){
            if (nums.has(value - 1)){
                
            }
            else{
                let length = 1
                let n = value + 1
                while (nums.has(n)){
                    length += 1
                    n = n + 1
                }

                maxlen = Math.max(maxlen, length)
              
            }
        }

        return maxlen
    }
}
