class Solution:
    def productExceptSelf(self, nums):

        left = [1] * len(nums)

        product = 1

        for i in range(len(nums)):
            left[i] = product
            product *= nums[i]

        answer = [1] * len(nums)

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = left[i] * product
            product *= nums[i]

        return answer