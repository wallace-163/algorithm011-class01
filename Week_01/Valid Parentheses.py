class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. once meets the right kuohao, should pop a left kuohao,
        2. to avoid the danyi case: contain only left or right, two lists are used to record the two extreme cases
        3. list can be used as a stack, list (pop), (del) the lastest added elements
        4. pop : memorize that the  object should not be empty
        5.  if aa.pop():
            elif aa.pop():
            aa has only one elemnts , but aa pop element at twice.
            aa = list.pop() independent of conditions
        6. one to return is not right-----> continue
        :param s:
        :return:
        """
        list_enter = []
        list_leave = []
        if s == '' or  s==' ':
            return True
        for item in s:
            if item == ' ':
                continue
            elif item == '{' or item =='[' or item =='(':
                list_enter.append(item)
            else:
                list_leave.append(item)
                if list_enter:
                    aa = list_enter.pop()
                    if aa == '{':
                         if item == '}':
                             del list_leave[-1]
                             continue
                    elif aa == '[':
                         if item == ']':
                             del list_leave[-1]
                             continue
                    else:
                        if item == ')':
                            del list_leave[-1]
                            continue

        if list_enter or list_leave:
            return False
        return True

if __name__ == '__main__':
    print(Solution().isValid(''))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid('()'))
    print(Solution().isValid('('))
    print(Solution().isValid(']'))
    print(Solution().isValid('([]'))


