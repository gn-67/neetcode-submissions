class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first thing we want to do is create an adajcency list of every course and its prereqs

        preMap = { i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        #we also want to create a set to track which nodes we visit during dfs traversal, to ensure we don't encounter a loop 

        visited = set()

        def dfs(course):
            if preMap[course] == []:
                return True
            
            if course in visited:
                return False

            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            preMap[course] == []
            return True


        for course, pre in prerequisites:
            if not dfs(course):
                return False    
        
        return True
        

        