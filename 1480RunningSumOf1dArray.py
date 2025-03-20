class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = [0] * len(nums)
        runningSum[0] = nums[0]

        for i in range(len(nums)-1):
            runningSum[i+1] = runningSum[i] + nums[i+1]

        return runningSum
    
    def runningSum2(self, nums):
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]

        return nums

def checkSol(result, expected):
    if result == expected:
        print('Correct!')
    else:
        print('Wrong!!!')

def main(args=None):
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 1, 1, 1, 1]
    nums3 = [8, 10, 1, 4, 23]

    nums1_sol = [1, 3, 6, 10]
    nums2_sol = [1, 2, 3, 4, 5]
    nums3_sol = [8, 18, 19, 23, 46]

    solution = Solution()

    res11 = solution.runningSum(nums1)
    res12 = solution.runningSum2(nums1)

    res21 = solution.runningSum(nums2)
    res22 = solution.runningSum2(nums2)

    res31 = solution.runningSum(nums3)
    res32 = solution.runningSum2(nums3)

    checkSol(res11,nums1_sol)
    checkSol(res12,nums1_sol)
    checkSol(res21,nums2_sol)
    checkSol(res22,nums2_sol)
    checkSol(res31,nums3_sol)
    checkSol(res32,nums3_sol)

if __name__ == '__main__':
    main()