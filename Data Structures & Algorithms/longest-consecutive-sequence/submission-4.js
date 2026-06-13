class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    
    //a starting point is only when nums[i] - 1 does not exist
    longestConsecutive(nums) {
        let result = 0
        let numSet = new Set(nums)

        for (let num of numSet){
            let count = 0
            if (numSet.has(num - 1)){
                continue
            }
            else{
                while (numSet.has(num)){
                    count += 1
                    num += 1
                }
                result = Math.max(result, count)
            }
        }
        return result 

    }
}
