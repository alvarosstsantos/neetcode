from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if (nums[j] != val):
                nums[i] = nums[j]
                i += 1

        return i


if __name__ == "__main__":
    s = Solution()

    test_input_1 = [3, 2, 2, 3]
    test_input_2 = [0, 1, 2, 2, 3, 0, 4, 2]

    assert s.removeElement(test_input_1, 3) == 2
    assert s.removeElement(test_input_2, 2) == 5
