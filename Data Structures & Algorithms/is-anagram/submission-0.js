class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const ar = []

        for (let i=0; i < s.length; i++) {
            const charCode = s.charCodeAt(i);

            if (ar[charCode]) {
                ar[charCode] += 1;
            } else {
                ar[charCode] = 1;
            }
        }

        for (let i=0; i < t.length; i++) {
            const charCode = t.charCodeAt(i);

            if (ar[charCode]) {
                ar[charCode] -= 1;
            } else {
                return false;
            }
        }

        const sum = ar.reduce((acc, each) => acc + each, 0);

        return !sum
    }
}
