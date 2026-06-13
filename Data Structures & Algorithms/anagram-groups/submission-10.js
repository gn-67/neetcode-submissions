class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    
    //will all letters be lowercase?

    //we could check the characters for each work, 
    //then group them by same character count within a hash map
    // then we can just return the .values() of our hashmap
    groupAnagrams(strs) {
        let anagrams = {}
        let charA = "a".charCodeAt(0)

        for(let i = 0; i < strs.length; i++){
            let char = Array.from({length : 26}).fill(0)
            for (let j = 0; j < strs[i].length; j++){
                char[strs[i].charCodeAt(j) - charA] += 1 //keep track of char count
            }
            char = char.toString() //since objects only take stings as keys
            if (char in anagrams){ 
                anagrams[char].push(strs[i])
            }
            else{
                anagrams[char] = [strs[i]]
            }
        }

        return Object.values(anagrams)


















    }
}