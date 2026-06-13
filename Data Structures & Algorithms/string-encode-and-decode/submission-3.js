class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    // embed information in the encoding
    encode(strs) {
        //needs to output a string
        let result = ""
        for (let i = 0; i < strs.length; i++){
            let n = strs[i].length
            result += String(n)
            result += "#"
            result += strs[i]
        }
        return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        //needs to take in string and output array
        let result = []
        for (let i = 0; i<str.length; i++){
            let n = ""
            while (str[i] != "#"){
                n += str[i] 
                i += 1
                continue
            }
            result.push(str.slice(i + 1, i + 1 + Number(n)))
            i = i + Number(n)

        }

        return result

    }
}
