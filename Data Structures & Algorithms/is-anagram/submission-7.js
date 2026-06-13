class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const d1 = {}
        const d2 = {}
        if (s.length != t.length){
            return false
        }
        for (let i = 0; i < s.length; i++){
            if (s[i] in d1) {
                d1[s[i]] += 1
            }
            else {
                d1[s[i]] = 1
            }
            if (t[i] in d2) {
                d2[t[i]] += 1
            }
            else {
                d2[t[i]] = 1
            }
        }
        for (let key in d1){
            if (d1[key] !== d2[key]){
                return false
            }
        }
        return true
    }
}
