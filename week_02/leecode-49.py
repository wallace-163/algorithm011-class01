from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted(strs, key= lambda x: len(x), reverse=False)
        # aa = []
        # for i in range(1,len(strs)):
        #     bb = [strs[0]]
        #     if len(strs[i]) == len(strs[i-1]):
        #         bb.append(strs[i])
        #     else:
        #         continue

        group_dict = dict()
        while strs:
            index_set_kept = []
            group_dict[strs[0]] = []
            for i in range(len(strs)):
                if self.isAnagram(strs[0], strs[i]):
                    group_dict[strs[0]].append(strs[i])
                else:
                    index_set_kept.append(i)
            if  index_set_kept:
                strs = [strs[i] for i in index_set_kept]
            else:
                strs = []
        aa = sorted(group_dict.items(), key = lambda x: len(x), reverse = False)
        return [item[1] for item in aa]


    def isAnagram(self, s: str, t: str) -> bool:
        if not s and t:
            return False
        if s and not t:
            return False
        if not s and not t:
            return True
        dict_s = dict()
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 0
        dict_t = dict()
        for j in t:
            if j in dict_t:
                dict_t[j] += 1
            else:
                dict_t[j] = 0

        if set(dict_s) != set(dict_t):
            return False

        for k in dict_s:
            if k not in dict_t:
                return False
            else:
                if dict_s[k] != dict_t[k]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams(["compilations", "complainants"]))
    print("hello")
