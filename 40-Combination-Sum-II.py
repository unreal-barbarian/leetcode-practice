from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target:
            return []
        bins = Counter(candidates)
        numbers = list(bins.keys())
        # sort the list so that we try large numbers first
        numbers.sort(reverse=True)
        nums = []
        # remove any number larger than target
        for i, n in enumerate(numbers):
            if n <= target:
                nums += numbers[i:]
                break
        # if nothing left, return
        if len(nums) == 0:
            return []
        counts = [bins[n] for n in nums]

        return self.comb2(nums, counts, target, [])

    def comb2(self, nums, cnts, target, used):
        # nums: the numbers for each group
        # cnts: how many numbers in each group
        # target: target number to add up
        # used: the numbers in current trial combination
        answer = []
        if len(nums) == 0:
            return []
        num = nums[0]
        cnt = cnts[0]
        # note that python use reference for list, no extra memory cost here
        if target == 0:
            return [used]
        # speed up
        # no need to try all combination of this group of numbers
        if num * cnts[0] > target:
            cnts[0] = target // num
        # if current number cannot add to target, move to next number
        if num > target:
            return self.comb2(nums[1:], cnts[1:], target, used)
        # This might improve speed a little bit, but not worth the trouble
        # if num == target:
        #     return [used + [num]] + self.comb2(nums[1:], cnts[1:], target, used)

        # another speed up
        # if this is the last group of numbers, return the result directly
        # apparently, if target can be fully divided, return the result; otherwise no solution
        if len(nums) == 1:
            if target % num == 0 and num * cnt >= target:
                return [used + [num] * (target // num)]
            else:
                return []

        # core recursion
        # try every possible counts of the current number
        # this loop can also be written in recursion to eliminate the "for"
        for i in range(cnts[0] + 1):
            diff = target - i * num
            subans = self.comb2(nums[1:], cnts[1:], diff, used + [num] * i)
            answer += subans
        return answer


a = Solution()
print(a.combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6))
print(a.combinationSum2([2, 5, 2, 1, 2], 5))
print(a.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(a.combinationSum2([1, 1, 1, 1, 1, 1], 5))
