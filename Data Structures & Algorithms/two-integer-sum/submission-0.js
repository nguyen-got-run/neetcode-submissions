class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const complement = {}
        const answer = []

        for (let i=0; i < nums.length; i++) {
            const num = nums[i];
            const diff = target - num;

            if (diff in complement) {
                const idx = complement[diff];
                answer.push(...[i, idx])
                break;
            } else {
                complement[num] = i
            }
        }

        return answer
    }
}
