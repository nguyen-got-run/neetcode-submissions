class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const ar = [];

        for (const num of nums) {
            if (ar[num]) {
                return true;
            } else {
                ar[num] = 1
            }
        }

        return false
    }
}
