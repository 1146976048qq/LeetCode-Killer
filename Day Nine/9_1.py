
# 207. 课程表
# ***************************************
# 班级里有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
# ***************************************
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# ***************************************
# 输入：
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出：2
# 解释：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。
# ***************************************
# 输入：
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出：1
# 解释：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，这是所有学生中的一个朋友圈。
# ***************************************
# https://leetcode-cn.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        n = len(M)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] and not visited[j]:
                visited[j] = True
                self.dfs(M, visited, j)


print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
print("***************************************")