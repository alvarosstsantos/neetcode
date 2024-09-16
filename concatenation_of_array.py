from typing import List


class Solution(object):
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = len(nums)
        y = [None] * (x * 2)

        for i in range(x):
            y[i] = nums[i]
            y[x + i] = nums[i]

        return y


if __name__ == "__main__":
    s = Solution()

    test_input_1 = [1, 2, 1]
    test_input_2 = [1, 3, 2, 1]

    assert s.getConcatenation(test_input_1) == [1, 2, 1, 1, 2, 1]
    assert s.getConcatenation(test_input_2) == [1, 3, 2, 1, 1, 3, 2, 1]
