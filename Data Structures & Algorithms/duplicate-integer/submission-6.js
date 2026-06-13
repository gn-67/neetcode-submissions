class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */

    //ok so I think a data strucutre that would be most appropriate here would be a Set() as sets do not contain duplicates
    //so I will convert the dataset into a set and see if their lengths differ then that means a value was removed 
    hasDuplicate(nums) {
        let setNums = new Set(nums)
        if (setNums.size !== nums.length){
            return true
        }
        return false
    }
}
