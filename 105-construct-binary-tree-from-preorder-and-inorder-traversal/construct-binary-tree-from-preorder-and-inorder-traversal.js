var buildTree = function(preorder, inorder) {
    // Map value -> index in inorder
    const indexMap = new Map();
    for (let i = 0; i < inorder.length; i++) {
        indexMap.set(inorder[i], i);
    }

    let preIndex = 0;

    function helper(left, right) {
        if (left > right) return null;

        // Root value from preorder
        const rootVal = preorder[preIndex++];
        const root = new TreeNode(rootVal);

        // Index in inorder
        const mid = indexMap.get(rootVal);

        // Build subtrees
        root.left = helper(left, mid - 1);
        root.right = helper(mid + 1, right);

        return root;
    }

    return helper(0, inorder.length - 1);
};
