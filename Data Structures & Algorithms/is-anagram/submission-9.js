class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */

    //since we are checking if two elements contain the same exact character
    // i think we should create an object for each string with the letter as the key and the frequency of each letter as the value
    // then we can compare the two objects and if they differ we return false, otherwise we return true    
    isAnagram(s, t) {
        let sHash = {}
        let tHash = {}

        if (s.length !== t.length){
            return false
        }

        for (let i = 0; i < s.length; i++){
            if (s[i] in sHash){
                sHash[s[i]] += 1
            }
            else if (s[i] in sHash === false){
                sHash[s[i]] = 1
            }
            if (t[i] in tHash){
                tHash[t[i]] += 1
            }
            else if (t[i] in tHash === false){
                tHash[t[i]] = 1
            }
        }

        for (let key of Object.keys(sHash)){
            if (sHash[key] !== tHash[key]){
                return false
            }
        }
        return true

    }
}
