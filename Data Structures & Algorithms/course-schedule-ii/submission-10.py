class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i : [] for i in range(numCourses)}
        visited = set()
        cycle = set()
        result = []
        for preReq in prerequisites:
            preMap[preReq[0]].append(preReq[1])






        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)

            for preReq in preMap[node]:
                if not dfs(preReq):
                    return False

            cycle.remove(node)
            #we are no longer on this cycle^
            #we can use memoization to mark that this node is completable
            preMap[node] = []
            visited.add(node)
            result.append(node)
            return True
        
        #we need to make sure each course is completable
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result