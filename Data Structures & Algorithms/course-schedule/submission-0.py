class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first thing we want to do is layout our courses and prerequisites within an adjacency list
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
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
                
            visited.remove(course)  #why do we do this? i thought we check cycles bc the course was never marked “satisfiable”, so we return false when we visit it a second time
            preMap[course] == [] #its satisfiable

            return True

        
        for course, pre in prerequisites:
            if not dfs(course):
                return False

        return True

            
