import copy
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []     # 将res 设置成全局变量
        used = [False for _ in nums]
        path = []
        self.dfs(nums, 0, used, path, res)
        return  res

    def dfs(self, nums:List[int],depth: int, used: List[bool], path, res ):
        if len(path) == len(nums):
            res.append(copy.deepcopy(path))  # changeable object attention!!!
            return
        for i in range(len(nums)):
            if used[i] is True:
                continue
            else:
                path.append(nums[i])
                used[i] = True
                self.dfs(nums, depth + 1, used, path, res)
                path.pop()
                used[i] = False




if __name__ == '__main__':
    aa =Solution()
    print(aa.permute([1,2,3]))

