from typing import List
class SS:
    def mz(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[j] = nums[i]
                j += 1
        for k in range(j,len(nums)):
            nums[k] = 0




