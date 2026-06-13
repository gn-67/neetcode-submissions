class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    
    //since we need to be able to decode the string and be able to split up our string into the appropriate word lengths
    // we can encode some additional information into our string, that way when we are iterating through we know the appropriate length to split our words
    encode(strs) {
        let string = ""
        for (let i = 0; i < strs.length; i++){
            string += String(strs[i].length)
            string += "#"
            string += strs[i]
        }
        return string
    }
    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let result = []
        for (let i = 0; i < str.length; i++){
            let size = ""
            while (str[i] !== "#"){
                size += str[i]
                i += 1
            }
            result.push(str.slice(i + 1, i + 1 + Number(size)))
            i = i + Number(size)
        }
        return result

    }

}