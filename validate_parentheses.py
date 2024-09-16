class Solution(object):
    def isValid(self, s: str) -> bool:
        parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c not in parentheses:
                stack.append(c)
                continue
            elif not stack or parentheses[c] != stack[-1]:
                return False
            stack.pop()

        return True


if __name__ == "__main__":
    s = Solution()

    test_input_1 = "[]"
    test_input_2 = "]"

    assert s.isValid(test_input_1)
    assert not s.isValid(test_input_2)
