class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    //take count of each word 
    // use alphabet and if the alpha array exists, append the word to the list
    //return all values in an array
    groupAnagrams(strs) {
        let anagrams = new Map()
        const charCodeA = 'a'.charCodeAt(0)

        for (let i = 0; i < strs.length; i++){
            let a = new Array(26).fill(0)
            for (let j = 0; j < strs[i].length; j++){
                a[strs[i].charCodeAt(j) - charCodeA] += 1
            }
            let key = a.toString()
            if (anagrams.has(key)) {
                let existingArray = anagrams.get(key) //creates a reference to the value, which means we can directly modify it
                existingArray.push(strs[i])
            }
            else{
                anagrams.set(key,[strs[i]])
            }
        }

        return Array.from(anagrams.values())
    }
}
