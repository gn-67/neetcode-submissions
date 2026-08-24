class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #first we want to map out our courses and our prerequistes into an adjMap
        #then I will use a DFS function and run it on every course in our course list, ensuring that no path contains a cycle
        #I will remove courses from our cycle path so it can be used again

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

            for preReq in adjMap[node]:
                if not dfs(preReq):
                    return False
            
            cycle.remove(node)
            visited.add(node)
            result.append(node)
            return True



        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result