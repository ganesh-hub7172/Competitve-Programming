var longestPalindrome = function (s) {
    if (!s || s.length === 0) return "";

    let res = "";

    function expand(left, right) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return s.substring(left + 1, right);
    }

    for (let i = 0; i < s.length; i++) {
        // Odd length palindrome
        let p1 = expand(i, i);
        // Even length palindrome
        let p2 = expand(i, i + 1);

        if (p1.length > res.length) res = p1;
        if (p2.length > res.length) res = p2;
    }

    return res;
};