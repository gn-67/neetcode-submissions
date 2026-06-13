class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */

    //can k be 0? can the input array be empty
    // we can track frequencies using a hashmap
    // then we can get the entries, sort by values, and return the top k keys
    
    topKFrequent(nums, k) {
        let count = {}
        let result = []
        for (let i = 0; i < nums.length; i++){
            if (nums[i] in count){
                count[nums[i]] += 1
            }
            else{
                count[nums[i]] = 1
            }
        }

        let counts = Object.entries(count).sort((a, b) => b[1]-a[1]) //descending order
        for (let i = 0; i < k; i++){
            result.push(counts[i][0])
        }

        return result
    }
}
