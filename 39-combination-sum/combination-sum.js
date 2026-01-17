var combinationSum = function(candidates, target) {
    const res = [];

    function backtrack(start, path, remaining) {
        if (remaining === 0) {
            res.push([...path]); // found a valid combination
            return;
        }
        if (remaining < 0) return; // exceeded target, stop

        for (let i = start; i < candidates.length; i++) {
            path.push(candidates[i]);             // choose the number
            backtrack(i, path, remaining - candidates[i]); // same number can be reused
            path.pop();                           // backtrack
        }
    }

    backtrack(0, [], target);
    return res;
};
