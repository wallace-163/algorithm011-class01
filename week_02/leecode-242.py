class Solution:
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
    print(Solution().isAnagram("compilations", "complainants"))