class Solution(object):
    def containsDuplicate(self, nums):
        seen = list(set(nums))
        if len(seen) == len(nums) :
            return False
        else : 
            return True  