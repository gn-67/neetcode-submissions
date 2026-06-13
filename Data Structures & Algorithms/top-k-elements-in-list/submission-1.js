class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    //lets use a hash map holding the frequency of each element within the array
    // we sort by values and return the a
    topKFrequent(nums, k) {
        let freq = {}
        for (let i = 0; i < nums.length; i++){
            if (nums[i] in freq){
                freq[nums[i]] += 1
            }
            else{
                freq[nums[i]] = 1
            }
        }

        let pairs = Object.entries(freq)
        pairs.sort((pair1, pair2) => {
            return pair2[1] - pair1[1]
        })

        let result = []
        for (let i = 0; i < k; i++){
            result.push(pairs[i][0])

        }

        return result
    }
}
