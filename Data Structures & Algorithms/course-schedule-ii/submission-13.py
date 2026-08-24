class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjMap = {i : [] for i in range(numCourses)}

        for prereq in prerequisites:
            adjMap[prereq[0]].append(prereq[1])

        
        cycle = set()
        visited = set()

        result = []

        def dfs(node):
            if node in cycle:
                return False
            
            if node in visited:
                return True


            cycle.add(node)
            for course in adjMap[node]:
                if not dfs(course):
                    return False
            
            cycle.remove(node)
            visited.add(node)
            result.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return result