import unittest


class MedianUtil(object):
    def getNumbers(self):
        # Bob's implementation
        f = open("numbers.txt", 'r')
        nums = f.readlines()
        return [int(i) for i in nums]

    def getMedian(self):
        # Alice's implementation
        nums = self.getNumbers()
        mid_index = len(nums) // 2
        return (nums[mid_index] + nums[mid_index - 1]) / 2 if mid_index % 2 == 0 else nums[mid_index]


class TestMedium(unittest.TestCase):
    def testGetMedian(self):
        def mockGetMedian(self):
            nums = self.getNumbers()
            print(nums)
            return 4

        _getMedian = MedianUtil.getMedian
        try:
            MedianUtil.getMedian = mockGetMedian
            util = MedianUtil()
            self.assertEqual(4, util.getMedian())
        finally:
            MedianUtil.getMedian = _getMedian

    def testGetNumbers(self):
        def mockGetNumers(self):
            return [i for i in range(1, 8)]

        _getNumbers = MedianUtil.getNumbers
        try:
            MedianUtil.getNumbers = mockGetNumers
            util = MedianUtil()
            self.assertEqual(4, util.getMedian())
        finally:
            MedianUtil.getNumbers = _getNumbers


if __name__ == "__main__":
    unittest.main()
