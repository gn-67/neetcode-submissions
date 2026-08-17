class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first I will create an adjacency map to map out each node and its respective prereqs
        #then I will use a DFS algorithm to traverse each course
            #base case is if the course doens't have any prereqs, we can complete it
        #additionally, we can use a set to track which nodes we've visited, ensuring we don't reach a loop
        #if we do reach a loop in our traversal, that means one course depends on another course which depends on the original course, meaning its incompletable
        #we need to ensure this is a DAG

        preMap = {i : [] for i in range(numCourses)}
        visited = set()
        for preReq in prerequisites:
            preMap[preReq[0]].append(preReq[1])

        def dfs(node):
            if preMap[node] == []:
                return True
            if node in visited:
                return False

            visited.add(node)
            for preReq in preMap[node]:
                if not dfs(preReq):
                    return False
            #we can use memoization to mark that this node is completable
            preMap[node] = []
            return True
        
        #we need to make sure each course is completable
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

            


        