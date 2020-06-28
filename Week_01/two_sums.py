class Solution(object):
    def twoSum(self, nums, target):
        rest_index_dict = {}
        for i, value in enumerate(nums):
            rest = target - value
            if rest in rest_index_dict:
                return [i, rest_index_dict[rest]]
            else:
                rest_index_dict[value] = i


