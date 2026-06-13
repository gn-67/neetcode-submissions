class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = []
        for (let i = 0; i < s.length; i++){
            if (s[i] === ')'){
                let top = stack.pop()
                if (top !== '('){
                    return false
                }
            }
            else if (s[i] === '}'){
                let top = stack.pop()
                if (top !== '{'){
                    return false
                }
            }
            else if (s[i] === ']'){
                let top = stack.pop()
                if (top !== '['){
                    return false
                }
            }
            else{
                stack.push(s[i])
            }
        }

        if (stack.length !== 0 ){
            return false
        }

        return true
    }
}
