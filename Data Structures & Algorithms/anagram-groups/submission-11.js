class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    //since we only care about matching words with the exact same character frequencies
    // we can track the count of each letter within the words and add that to a Object with the actual word as its value
    // so any words with the same frquency of letters will be grouped into an array as a value
    //then we just return the values of this object!
    groupAnagrams(strs) {
        let groups = {}
        let codeA = 'a'.charCodeAt(0)
        
        for (let i = 0; i < strs.length; i++){
            let charCount = Array(26).fill(0)

            for (let j = 0; j < strs[i].length; j++){
                charCount[strs[i].charCodeAt(j) - codeA] += 1
            }

            charCount = charCount.toString()

            if (charCount in groups){
                groups[charCount].push(strs[i])
            }
            else{
                groups[charCount] = [strs[i]]
            }
        }

        return Object.values(groups)
    }
}
