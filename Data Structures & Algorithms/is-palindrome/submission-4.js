class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.split("")
        s = s.filter(char => /^[a-z0-9]*$/gi.test(char))

        let left = 0
        let right = s.length - 1

        while (left <= right){
            if (s[left].toLowerCase() !== s[right].toLowerCase()){
                return false
            }
            else{
                left += 1
                right -= 1
            }
        }

        return true

    }
}
