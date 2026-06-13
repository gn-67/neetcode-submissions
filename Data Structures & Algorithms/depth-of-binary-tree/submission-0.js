/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */

    //we can use a depth first search algorithm here
    maxDepth(root) {
        if (!root){
            return 0
        }

        return 1 + Math.max(this.maxDepth(root.left), this.maxDepth(root.right))
        

    }
}
