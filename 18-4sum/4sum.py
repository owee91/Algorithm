class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        output = set()

        for i in range(n):
            for j in range(i+1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] == target:
                        output.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1

        return output