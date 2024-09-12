from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1

                nums[i] = nums[j]

        return i + 1


if __name__ == "__main__":
    s = Solution()

    test_input_1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    test_input_2 = [1, 1, 2]

    assert s.removeDuplicates(test_input_1) == 5
    assert s.removeDuplicates(test_input_2) == 2
