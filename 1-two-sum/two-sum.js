
// Musham Ganesh 
var twoSum = function(nums, target) {
    const map = new Map(); // stores value → index

    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];

        if (map.has(complement)) {
            return [map.get(complement), i];
        }

        map.set(nums[i], i);
    }
};
