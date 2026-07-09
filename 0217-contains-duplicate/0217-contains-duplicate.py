class Solution(object):
    def containsDuplicate(self, nums):
        seen = set(nums)
        if len(seen) == len(nums) :
            return False
        else : 
            return True  