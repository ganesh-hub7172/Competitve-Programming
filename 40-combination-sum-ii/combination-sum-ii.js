var combinationSum2 = function(candidates, target) {
    const res = [];
    candidates.sort((a, b) => a - b); // sort to handle duplicates

    function backtrack(start, path, remaining) {
        if (remaining === 0) {
            res.push([...path]);
            return;
        }

        for (let i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] === candidates[i - 1]) continue; // skip duplicates
            if (candidates[i] > remaining) break; // early pruning

            path.push(candidates[i]);
            backtrack(i + 1, path, remaining - candidates[i]); // use next index
            path.pop();
        }
    }

    backtrack(0, [], target);
    return res;
};
