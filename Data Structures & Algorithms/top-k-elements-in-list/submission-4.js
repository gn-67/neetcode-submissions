class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */

    // i think we can iterate over nums and create an object tracking each number and its frequency
    //then we can sort the values in descending order and return the k elements
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

        let sorted = Object.entries(count).sort((a,b) => b[1] - a[1])

        for (let i = 0; i < k; i++){
            result.push(sorted[i][0])
        }

        return result
        
    }
}



