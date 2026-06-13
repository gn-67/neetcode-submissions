class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    //can i saftely assume that the input array is in sorted order

    //we return the inex of the compiment that we saw earlier in the array first since that is the smaller index, then the index of the current value that needs this compliment value to add up to the target
    // we can use an object datastructure to keep track fo the values that we have seen
    twoSum(nums, target) {
        let seen = {}
        for (let i = 0; i < nums.length; i++){
            let compliment = target - nums[i]
            if (compliment in seen){
                return [seen[compliment], i]
            }
            else{
                seen[nums[i]] = i
            }
        }
        
    }
}
