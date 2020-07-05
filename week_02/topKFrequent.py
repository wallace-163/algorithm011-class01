from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index_dict = dict()
        for i in nums:
            if i in index_dict:
                index_dict[i] += 1
            else:
                index_dict[i] = 1
        assert k <= len(index_dict), "wrong input"
        list = []
        for key, value in index_dict.items():
            heapq.heappush(list, (value, key))
        return [item[1] for item in heapq.nlargest(k, list)]


if __name__ == '__main__':
    print(Solution().topKFrequent([1,2,2,3,3], 2))