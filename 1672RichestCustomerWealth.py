class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        biggestWealth = 0

        for i in range(len(accounts)):
            currentWealth = 0
            for j in range(len(accounts[i])):
                currentWealth += accounts[i][j]
            if currentWealth > biggestWealth:
                biggestWealth = currentWealth

        return biggestWealth
    
    def maximumWealth2(self, accounts):
        return max(sum(x) for x in accounts)
    
def checkSol(result, expected):
    if result == expected:
        print("Correct!!")
    else:
        print("Wrong")

def main(args=None):
    acc1 = [[1,2,3],[3,2,1]]
    acc2 = [[1,5],[7,3],[3,5]]
    acc3 = [[2,8,7],[7,1,3],[1,9,5]]

    acc1Sol = 6
    acc2Sol = 10
    acc3Sol = 17

    solution = Solution()

    res11 = solution.maximumWealth(acc1)
    res12 = solution.maximumWealth2(acc1)

    res21 = solution.maximumWealth(acc2)
    res22 = solution.maximumWealth2(acc2)

    res31 = solution.maximumWealth(acc3)
    res32 = solution.maximumWealth2(acc3)

    checkSol(res11, acc1Sol)
    checkSol(res12, acc1Sol)

    checkSol(res21, acc2Sol)
    checkSol(res22, acc2Sol)

    checkSol(res31, acc3Sol)
    checkSol(res32, acc3Sol)

if __name__=="__main__":
    main()