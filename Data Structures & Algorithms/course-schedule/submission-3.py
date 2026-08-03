class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first we want to unpack what each courses prereqs are through and adj list
        #if we encounter a cycle, one course depending on another course which dpeneds on the original course, we can return false because this is imposible to satisfy




        reqMap = { i : [] for i in range(numCourses)}

        for i in range(len(prerequisites)):
            reqMap[prerequisites[i][0]].append(prerequisites[i][1])
        
        #now we can write our dfs functinon, using an empty set to track courses we know are completable

        visited = set()

        def dfs(course):
            if course in visited:
                return False
                #we have already visited this course in our path 
            
            if reqMap[course] == []:
                return True #the course doesn't have any pre reqs
            
            visited.add(course)
            for prereq in reqMap[course]:
                if not dfs(prereq):
                    return False
            #clean up
            visited.remove(course)
            #so does visited clear on each course run?
            reqMap[course] = []
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

