from typing import List
from heapq import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        list =[]
        list_max = []
        for i in nums:
            if len(list) < k:
                heappush(list,i)
            else:
                list_max.append(nlargest(1,list)[0])
                heapreplace(list, i)
        list_max.append(nlargest(1,list)[0])  
        return list_max


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([7,2,4], 2))
