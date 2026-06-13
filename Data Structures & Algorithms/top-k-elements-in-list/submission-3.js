class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */

    //im thinking we can utilize an object here to keep track of each element and its frequency
    //then we get the entries sort it in descning order and return the top k ones
    topKFrequent(nums, k) {
        let count = {}
        let result = []
        for (let i = 0; i < nums.length; i++){
            if (nums[i] in count){
                count[nums[i]] += 1
            }
            else{
                count[nums[i]] = 0
            }
        }

        let entries = Object.entries(count).sort((a,b) => (b[1] - a[1]))

        for (let i = 0; i < k; i++){
            result.push(entries[i][0])
        }
        return result

    }
}
