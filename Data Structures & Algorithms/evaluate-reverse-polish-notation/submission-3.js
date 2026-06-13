class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    //since we are evaluating previous elements I think a stack data structure would be hlepful here
    // we can push numbers to the stack and when we reach an operation we can pop the last two values and perform the operation
    // then push the new value back onto stack
    // we can also use an object for o(1) lookup of operation
    evalRPN(tokens) {
        let stack = []
        let operators = { "+" : (x, y) => x + y, "-" : (x,y) => x - y, "*" : (x,y) => x * y, "/" : (x,y) => Math.trunc(x / y)}
        for (let i = 0; i < tokens.length; i++){
            if (tokens[i] in operators){
                let y = Number(stack.pop())
                let x = Number(stack.pop())
                let total = operators[tokens[i]](x, y)
                stack.push(total)
            }
            else{
                stack.push(tokens[i])
            }
        }
        return stack[0] //the remaining value should be the result of the operation
    }
}
