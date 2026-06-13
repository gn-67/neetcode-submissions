class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */

    //we can add each character to a hashmap tracking the char and its count
    //then compare the two hashmaps, if they are different
    // one edge case is if they have different lengths we automatically can return false
    isAnagram(s, t) {
        let sCount = {}
        let tCount = {}

        if (s.length !== t.length){
            return false
        }

        for (let i = 0; i < s.length; i++){
            if (s[i] in sCount){
                sCount[s[i]] += 1
            }
            else if (s[i] in sCount === false){
                sCount[s[i]] = 1
            }
            if (t[i] in tCount){
                tCount[t[i]] += 1
            }
            else if (t[i] in tCount === false){
                tCount[t[i]] = 1
            }
        }

        for (let key of Object.keys(sCount)){
            if (sCount[key] !== tCount[key]){
                return false
            }
        }

        return true

    } 
}
